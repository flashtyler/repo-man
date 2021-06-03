from django.urls import path
from todo.views import index, edit_todo, delete_todo

urlpatterns = [
    path("", index, name="index"),
    path("delete/<int:pk>/", delete_todo, name="delete_todo"),
    path("edit/<int:pk>/", edit_todo, name="edit_todo"),
]