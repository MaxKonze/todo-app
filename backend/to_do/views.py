from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoItem
from django.views.generic import ListView

new_todo = {}


def to_dos(request):
    global new_todo

    if request.method == 'POST':
        
        print(request.POST)
        #if request.POST == 'edit':
        #    print("done")

        new_todo = dict(request.POST)

        ToDoItem.objects.create(
            title=new_todo['title'][0],
            datetime=new_todo['datetime'][0],
            location=new_todo['location'][0],
            describtion=new_todo['describtion'][0])
        

    return render(request, 'to_do_list.html')


def to_do_list(request):
    items = ToDoItem.objects.all()
    return render(request,template_name="",context={"to_dos":items})

def new_todo(request):
    return render(request,'new_todo.html')