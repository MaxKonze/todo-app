from django.db import models



# Create your models here.
class ToDoList(models.Model):
    """
    A model of a hole ToDoList for a single user
    """

    created_at  = models.DateTimeField(auto_created=True,auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    completed   = models.BooleanField(default=False)


class ToDoItem(models.Model):
    """
    A model of a single todo with all its atributes
    """
    todo_list = models.ForeignKey(to=ToDoList,null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,default='')
    completed = models.BooleanField(default=False)
    datetime = models.CharField(max_length=30,default='')
    location = models.CharField(max_length=100,default='')
    describtion = models.CharField(max_length=500,default='')

