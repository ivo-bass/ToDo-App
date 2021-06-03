from django.contrib import admin
from django.urls import path

from todo_app.todos.views import index

urlpatterns = [
    path('', index)
]
