from django.db import models

from .category import Category
from .person import Person


class Todo(models.Model):
    title = models.CharField(
        max_length=30,
    )

    state = models.BooleanField(
        default=False,
    )

    description = models.TextField(
        null=True,
    )

    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True,
    )

    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title} / {self.owner}"
