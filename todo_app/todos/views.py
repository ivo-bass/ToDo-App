from django.shortcuts import render, redirect

from todo_app.todos.models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'index.html', context)


def create_todo(request):
    title = request.POST['title']
    description = request.POST['description']
    due_date = request.POST['due-date']
    priority = request.POST['priority']
    category = request.POST['category']

    todo = Todo(
        title=title,
        description=description,
        due_date=due_date,
        priority=priority,
        category=category,
    )
    todo.save()

    return redirect(index)


def change_state(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.state = not todo.state
    todo.save()
    return redirect(index)


def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect(index)

# TODO 1: Add EDIT SCREEN
# TODO 2: SORT BY DUE DATE
# TODO 3: SORT BY CATEGORY
# TODO 4: ADD HISTORY
