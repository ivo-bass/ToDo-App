from django.urls import path

from todo_app.todos.views import index, change_state, delete_todo, dashboard_page, add_todo_page, \
    details_page, delete_confirm, edit_todo_page, update_todo, history_page

urlpatterns = [
    path('', index),
    path('history/', history_page, name='history'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('add-todo/', add_todo_page, name='add-todo'),
    path('edit/<int:pk>', edit_todo_page, name='edit'),
    path('update/<int:pk>', update_todo, name='update'),
    path('details/<int:pk>', details_page, name='details'),
    path('history/details/<int:pk>', details_page),
    path('change-state/<int:pk>', change_state),
    path('delete-confirm/<int:pk>', delete_confirm),
    path('delete-todo/<int:pk>', delete_todo),
]
