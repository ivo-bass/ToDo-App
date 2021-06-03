from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=30)
    state = models.BooleanField(default=False)
