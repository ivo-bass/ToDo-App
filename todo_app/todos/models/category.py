from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=20,
        null=True,
    )

    class Meta:
        verbose_name_plural = 'categories'
