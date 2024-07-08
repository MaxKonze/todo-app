from django.contrib import admin
from to_do.models import ToDoItem, ToDoList
# Register your models here.

admin.site.register([ToDoList,ToDoItem])