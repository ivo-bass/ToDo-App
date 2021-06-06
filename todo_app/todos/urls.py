from django.urls import path

from todo_app.todos.views import index, create_todo, change_state, delete_todo, dashboard_page, add_todo_page, \
    details_page, delete_confirm, edit_todo_page, update_todo

urlpatterns = [
    path('', index),
    path('dashboard/', dashboard_page),
    path('add-todo/', add_todo_page),
    path('create/', create_todo),
    path('edit/<int:pk>', edit_todo_page),
    path('update/<int:pk>', update_todo),
    path('details/<int:pk>', details_page),
    path('change-state/<int:pk>', change_state),
    path('delete-confirm/<int:pk>', delete_confirm),
    path('delete-todo/<int:pk>', delete_todo),
]
