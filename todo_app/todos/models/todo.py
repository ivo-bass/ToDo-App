from django.db import models

from django.utils import timezone


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

    due_date = models.DateField(
        default=timezone.now,
    )

    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Normal', 'Normal'),
        ('Urgent', 'Urgent'),
    )
    priority = models.CharField(
        max_length=20,
        default='Normal',
        choices=PRIORITY_CHOICES,
    )

    CATEGORY_CHOICES = (
        ('Home', 'Home'),
        ('Family', 'Family'),
        ('Work', 'Work'),
        ('Study', 'Study'),
        ('Cars', 'Cars'),
        ('Friends', 'Friends'),
        ('Other', 'Other'),
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.title}"
