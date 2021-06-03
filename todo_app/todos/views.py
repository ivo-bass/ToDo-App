from django.shortcuts import render

from todo_app.todos.models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'index.html', context)
