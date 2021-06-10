from django.contrib import admin

from .models import Todo, Priority, Category


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_done', 'priority', 'category', 'due_date', ]
    list_filter = ['priority', 'is_done', 'category', ]
    sortable_by = ['title', 'is_done', 'priority', 'category', 'due_date', ]


admin.site.register(Todo, TodoAdmin)
admin.site.register(Priority)
admin.site.register(Category)