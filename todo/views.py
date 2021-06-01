from django.shortcuts import render, redirect
from .models import TodoList


def index(request):
    # Query all todolist items with the object manager.
    todos = TodoList.objects.all()

    # Check if the request method is a POST.
    if request.method == "POST":
        # Check if there is a request to add a a new todolist.
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            location = request.POST["location_select"]
            content = title + " -- " + date + " " + location
            Todo = TodoList(title=title, content=content, due_date=date, location=location)
            # Save the new todolist.
            Todo.save()
            # Reload the page.
            return redirect("/")

        # Check if there is a request to update an existing todolist.
        if "taskUpdate" in request.POST:
            # Get a list of all selected todolist items to be updated.
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                # Fetch the todolist.
                todo = TodoList.objects.get(id=int(todo_id))
                # Delete the todolist.
                todo.delete()

            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            location = request.POST["location_select"] # Location
            content = title + " -- " + date + " " + location # content
            Todo = TodoList(title=title, content=content, due_date=date, location=location)
            Todo.update() #update the todo
            # Reload the page.
            return redirect("/")

        # Check if there is a request to delete an existing todolist.
        if "taskDelete" in request.POST:
            # Get a list of all selected todolist items to be updated.
            checkedlist = request.POST["checkedbox"]

            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                # Delete the todolist.
                todo.delete()

    return render(request, "index.html", {"todos": todos})