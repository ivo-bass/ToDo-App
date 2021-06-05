from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'state', 'priority', 'category', 'due_date', ]
    list_filter = ['priority', 'state', 'category', ]
    sortable_by = ['title', 'state', 'priority', 'category', 'due_date', ]


admin.site.register(Todo, TodoAdmin)
