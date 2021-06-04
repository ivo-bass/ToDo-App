from django.db import models

from .category import Category


class Todo(models.Model):
    title = models.CharField(
        max_length=30,
    )

    state = models.BooleanField(
        default=False,
    )

    description = models.TextField(
        null=True,
        blank=True,  # can save in admin with blank field / not required
    )


    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"
