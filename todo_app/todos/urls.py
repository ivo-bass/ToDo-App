from django.urls import path

from todo_app.todos.views import index, create_todo, change_state, delete_todo, dashboard_page, add_todo_page, \
    details_page

urlpatterns = [
    path('', index),
    path('dashboard/', dashboard_page),
    path('add-todo/', add_todo_page),
    path('create/', create_todo),
    path('details/<int:pk>', details_page),
    path('change-state/<int:pk>', change_state),
    path('delete-todo/<int:pk>', delete_todo),
]
