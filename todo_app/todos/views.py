from datetime import timedelta

from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from django.utils.timezone import make_aware

from todo_app.todos.models import Todo, Priority, Category


def index(request):
    # !!! Important
    naive_datetime = datetime.today()
    naive_datetime += timedelta(days=1)
    aware_datetime = make_aware(naive_datetime)

    todos = Todo.objects.filter(due_date__lt=aware_datetime, state=False)
    todos.order_by('pk').order_by('due_date')
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)


def dashboard_page(request):
    naive_datetime = datetime.today()
    aware_datetime = make_aware(naive_datetime)

    todos = Todo.objects\
        .filter(due_date__gte=aware_datetime)\
        .order_by('pk')\
        .order_by('due_date')

    context = {
        'todos': todos,
    }
    return render(request, 'dashboard.html', context)


def add_todo_page(request):
    context = {
        'todos': Todo.objects.all(),
        'priorities': Priority.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'add.html', context)


def create_todo(request):
    title = request.POST['title']
    description = request.POST['description']
    due_date = request.POST['due-date']
    priority_name = request.POST['priority']
    category_name = request.POST['category']

    priority = Priority.objects.filter(name=priority_name).first()
    category = Category.objects.filter(name=category_name).first()

    todo = Todo(
        title=title,
        description=description,
        due_date=due_date,
        priority=priority,
        category=category,
    )
    todo.save()

    return redirect(dashboard_page)


def edit_todo_page(request, pk):
    todo = Todo.objects.get(pk=pk)
    # "%m/%d/%Y, %H:%M:%S" - proper symbols
    # yyyy-MM-ddThh:mm - expected format - "%Y-%m-%dT%H:%M"
    due_date = todo.due_date.strftime("%Y-%m-%dT%H:%M")

    context = {
        'date': due_date,
        'todo': todo,
        'priorities': Priority.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'edit.html', context)


def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.title = request.POST['title']
    todo.description = request.POST['description']
    todo.due_date = request.POST['due-date']
    # todo.state = request.POST['state']

    priority_name = request.POST['priority']
    category_name = request.POST['category']

    priority = Priority.objects.filter(name=priority_name).first()
    category = Category.objects.filter(name=category_name).first()

    todo.priority = priority
    todo.category = category
    todo.save()

    return redirect(dashboard_page)


def details_page(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'details.html', context)


def change_state(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.state = not todo.state
    todo.save()
    return redirect(dashboard_page)


def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect(dashboard_page)


def delete_confirm(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'delete-confirm.html', context)


def history_page(request):
    todos = Todo.objects.filter(state=True)
    todos.order_by('pk').order_by('due_date')
    context = {
        'todos': todos,
    }
    return render(request, 'history.html', context)
