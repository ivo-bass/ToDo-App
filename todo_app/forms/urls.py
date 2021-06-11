from django.urls import path

from todo_app.forms.views import show_form

urlpatterns = [
    path('', show_form, name="show form"),
]