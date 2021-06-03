from django.contrib import admin

from .models import Person, Category, Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'state']
    list_filter = ['owner', 'category']


admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)
