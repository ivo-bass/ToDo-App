from django.db import models

from django.utils import timezone
from django.utils.datetime_safe import time

from .category import Category
from .priority import Priority


class Todo(models.Model):
    title = models.CharField(
        max_length=30,
    )

    is_done = models.BooleanField(
        default=False,
    )

    description = models.TextField(
        null=True,
        blank=True,  # can save in admin with blank field / not required
    )

    due_date = models.DateTimeField(
        default=timezone.now,
    )

    date_created = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )


    # PRIORITY_CHOICES = ((obj.name, obj.name) for obj in Priority.objects.all())
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, null=True)

    # CATEGORY_CHOICES = ((obj.name, obj.name) for obj in Category.objects.all())
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"
