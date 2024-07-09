from django.db import models
from datetime import date



# Create your models here.
class ToDoList(models.Model):
    created_at  = models.DateTimeField(auto_created=True,auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    completed   = models.BooleanField(default=False)


class ToDoItem(models.Model):
    todo_list = models.ForeignKey(to=ToDoList,null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=date.today)
    label = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    time = models.TimeField(max_length=11, default=0)
    

