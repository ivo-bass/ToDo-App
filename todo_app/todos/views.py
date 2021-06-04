from django.shortcuts import render, redirect

from todo_app.todos.models import Todo, Person


def index(request):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'index.html', context)


def create_todo(request):
    title = request.POST['title']
    description = request.POST['description']
    owner_name = request.POST['owner']

    owner = Person.objects\
        .filter(name=owner_name)\
        .first()

    if not owner:
        owner = Person(name=owner_name)
        owner.save()

    todo = Todo(
        title=title,
        description=description,
        owner=owner,
    )
    todo.save()

    return redirect(index)


def change_state(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.state = not todo.state
    todo.save()
    return redirect(index)
