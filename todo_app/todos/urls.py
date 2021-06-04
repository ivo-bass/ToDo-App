from django.contrib import admin
from django.urls import path

from todo_app.todos.views import index, create_todo, change_state, delete_todo

urlpatterns = [
    path('', index),
    path('add-todo/', create_todo),
    path('change-state/<int:pk>', change_state),
    path('delete-todo/<int:pk>', delete_todo),
]
