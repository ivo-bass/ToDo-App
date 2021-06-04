from django.contrib import admin
from django.urls import path

from todo_app.todos.views import index, create_todo, change_state

urlpatterns = [
    path('', index),
    path('add-todo/', create_todo),
    path('change-state/<int:pk>', change_state),
]
