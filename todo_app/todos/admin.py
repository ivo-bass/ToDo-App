from django.contrib import admin

from .models import Todo, Priority, Category


class TodoAdmin(admin.ModelAdmin):
    # list_display = ['title', 'state', 'priority', 'category', 'due_date', ]
    # list_filter = ['priority', 'state', 'category', ]
    # sortable_by = ['title', 'state', 'priority', 'category', 'due_date', ]
    pass


admin.site.register(Todo, TodoAdmin)
admin.site.register(Priority)
admin.site.register(Category)