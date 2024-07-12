from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import ToDoItem


def to_do(request: HttpRequest, title: str) -> HttpResponse:
    """
     Renders the to-do item detail page based on the provided title

    Parameters:
        request (HttpRequest): The HTTP request object
        title (str): The title of the to-do item to be retrieved

    Returns:
        HttpResponse: The rendered todo page
    """

    todo = get_object_or_404(ToDoItem, title=title)

    return render(request, "to_do.html", context={"todo": todo})


def to_do_list(request):
    """
    Handles the display and creation of to-do items.

    POST request:
        Creates a new to-do item if the todo has a unique name

    Parameters:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: The rendered todo list page
    """

    new_todo = {}
    items = ToDoItem.objects.all()

    if request.method == "POST":
        new_todo = dict(request.POST)

        try:
            for item in items:
                if item.title == new_todo["title"][0]:
                    return render(
                        request,
                        template_name="to_do_list.html",
                        context={"to_dos": items},
                    )

            ToDoItem.objects.create(
                title=new_todo["title"][0],
                datetime=new_todo["datetime"][0],
                location=new_todo["location"][0],
                description=new_todo["description"][0],
            )

        except KeyError:
            pass

    items = ToDoItem.objects.all()
    return render(request, template_name="to_do_list.html", context={"to_dos": items})


def new_todo(request):
    """
    Handles the display of the form for a new todo

    Parameters:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: The rendered new todo page
    """

    return render(request, "new_todo.html")


def delete_todo(request, title):
    """
    Deletes a todo after clicking the delete Button

    Parameters:
        request (HttpRequest): The HTTP request object
        title (str): title of the todo

    Returns:
        HttpResponse: A redirect to the todo main page
    """

    ToDoItem.objects.filter(title=title).delete()

    return redirect("/to_do/")


def edit_todo(request, title):
    """_summary_

    Args:
        request (_type_): _description_
        title (_type_): _description_
    """
    item = get_object_or_404(ToDoItem, title=title)

    return render(request, "edit_todo.html", context={"todo": item})
