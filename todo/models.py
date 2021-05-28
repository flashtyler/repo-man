from django.db import models
from django.utils import timezone

class TodoList(models.Model): #Todolist able name that inherits models.Model
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    #location = models.ForeignKey(Location, default="general", on_delete=models.SET_DEFAULT) # a foreignkey
    location = models.CharField(max_length=100) # a varchar
    class Meta:
        ordering = ["-created"] #ordering by the created field
    def __str__(self):
        return self.title #name to be shown when called
