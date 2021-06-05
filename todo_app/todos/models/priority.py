from django.db import models


class Priority(models.Model):
    name = models.CharField(
        max_length=20,
        null=True,
    )

    class Meta:
        verbose_name_plural = 'priorities'
