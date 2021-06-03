from django.db import models
from django.utils import timezone


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    location = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    class Meta:
        # Order by the 'due_date' field.
        ordering = ["-due_date"]

    def __str__(self):
        # Name to be shown when called.
        return self.location
