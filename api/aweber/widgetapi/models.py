from django.db import models


class Widget(models.Model):
    name = models.CharField(max_length=64, blank=False)
    number_of_parts = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
