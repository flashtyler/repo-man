from django.shortcuts import render, redirect, render_to_response, HttpResponse
from .forms import TodoListForm
from .models import TodoList
import requests
import pandas


def weather():
    '''
    Call the weather API for the specified city locations.
    :return: A dictionary of weather data.
    '''
    locations = [
        "Aberdeen",
        "Birmingham",
        "Cardiff",
        "Dundee",
        "Guildford",
        "Plymouth",
        "Portsmouth",
        "Manchester",
        "Swansea",
        "Truro",
    ]
    weather_data = []
    api_key = "972d0342548784818117f8cea6d15f4e"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'

    for location in locations:
        # Request the API data and convert the JSON to Python data types.
        city_weather = requests.get(url.format(location, api_key)).json()

        weather = {
            'city': location,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        # Add the data for the current city into our list.
        weather_data.append(weather)

    # Convert the 'weather_data' list of dictionaries into a dictionary of lists.
    result = pandas.DataFrame(weather_data).to_dict(orient="records")

    return result


def index(request):
    '''
    The main view showing current to do tasks.
    :param request:
    :return:
    '''
    form = TodoListForm()

    if request.method == "POST":
        # Get the posted form.
        form = TodoListForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    todos = TodoList.objects.all()
    city_weather = weather()

    return render(request, "index.html", {"todo_form": form, "todos": todos, "city_weather": city_weather})


def edit_todo(request, pk):
    '''
    The view for editing a to do task.
    :param request:
    :param pk: The 'id' of the task to edit.
    :return:
    '''
    todo = TodoList.objects.get(id=pk)

    form = TodoListForm(instance=todo)

    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
            return redirect("index")

    city_weather = weather()

    return render(request, "edit_todo.html", {"todo_edit_form": form, "city_weather": city_weather})


def delete_todo(request, pk):
    '''
    Delete a to do task.
    :param pk: The 'id' of the task to delete.
    :return:
    '''
    todo = TodoList.objects.get(id=pk)
    # TODO  Add a confirmation prior to deleting.
    todo.delete()

    return redirect("index")
