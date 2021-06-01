from django.db import models
from django.utils import timezone


# Todolist table name that inherits models.Model
class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    #location = models.ForeignKey(Location, default="general", on_delete=models.SET_DEFAULT) # a foreignkey
    location = models.CharField(max_length=100) # a varchar

    class Meta:
        # order by the 'created' field.
        ordering = ["-created"]

    def __str__(self):
        # name to be shown when called.
        return self.title
