from django.db import models


# Create your models here.
class ToDoList(models.Model):
    """
    A model of a hole ToDoList for a single user

    Attributes:
    created_at (datetime):
    modified_at (datetime): The point in time when the list was modified
    completed (bool): Indicates whether the list is completed

    """

    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return


class ToDoItem(models.Model):
    """
    A model of a single todo with all its attributes

    Attributes:
    todo_list (Key): A reference to the related list
    created_at (datetime): The point in time when the todo was created
    title (str): The title of the task
    completed (bool): Indicates the status of the task
    datetime (datetime): The time when the todo would be done
    location (str): The location of the todo
    description (str): A detailed description of the todo

    """

    todo_list = models.ForeignKey(to=ToDoList, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default="")
    completed = models.BooleanField(default=False)
    datetime = models.CharField(max_length=30, default="")
    location = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=500, default="")

    def __str__(self) -> str:
        return
