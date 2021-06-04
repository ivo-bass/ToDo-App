from django.contrib import admin

from .models import Category, Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'state']
    list_filter = ['category']


admin.site.register(Todo, TodoAdmin)
admin.site.register(Category)
