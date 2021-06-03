from django.db import models

from .person import Person


class Todo(models.Model):
    text = models.CharField(max_length=30)
    state = models.BooleanField(default=False)
    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True
    )
