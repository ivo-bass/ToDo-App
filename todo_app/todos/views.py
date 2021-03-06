from datetime import timedelta

from django.forms import DateTimeInput
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from django.utils.timezone import make_aware

from todo_app.todos.forms import CreateTodoForm
from todo_app.todos.models import Todo, Priority, Category


def index(request):
    # today_todos = Todo.objects.filter(due_date__gte=datetime.date.now().replace(hour=0, minute=0, second=0))

    # !!! Important
    naive_datetime = datetime.today()
    current_time = make_aware(naive_datetime)
    naive_datetime = naive_datetime.replace(hour=23, minute=59, second=59)
    end_time = make_aware(naive_datetime)

    todos = Todo.objects \
        .filter(due_date__gte=current_time, due_date__lte=end_time) \
        .order_by('due_date')

    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)


def dashboard_page(request):
    naive_datetime = datetime.today()
    aware_datetime = make_aware(naive_datetime)

    todos = Todo.objects \
        .filter(due_date__gte=aware_datetime) \
        .order_by('due_date')

    context = {
        'todos': todos,
    }
    return render(request, 'dashboard.html', context)


def add_todo_page(request):
    if request.method == "GET":
        form = CreateTodoForm()
        return render(request, 'add.html', {'form': form})
    form = CreateTodoForm(request.POST)
    if form.is_valid():
        todo = form.save()
        todo.save()
        return redirect(dashboard_page)


def edit_todo_page(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        form = CreateTodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            todo.save()
            return redirect(dashboard_page)
    else:
        form = CreateTodoForm(instance=todo)
        form.fields['due_date'].widget.format = "%Y-%m-%dT%H:%M"

    context = {'form': form}
    return render(request, 'edit.html', context)


def delete_confirm(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == "POST":
        todo.delete()
        return redirect(dashboard_page)

    context = {'todo': todo}
    return render(request, 'delete-confirm.html', context)


def details_page(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'details.html', context)


def change_state(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect(dashboard_page)


def history_page(request):
    naive_datetime = datetime.today()
    aware_datetime = make_aware(naive_datetime)

    past_todos = Todo.objects.filter(due_date__lte=aware_datetime)
    done_todos = Todo.objects.filter(is_done=True)

    history_todos = past_todos.union(done_todos)

    history_todos.order_by('due_date')

    context = {
        'todos': history_todos,
    }
    return render(request, 'history.html', context)

# TODO: Separate navbar from base
