from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.todos.urls')),
    path('forms/', include('todo_app.forms.urls')),
]
