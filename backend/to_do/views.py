from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ToDoItem
from django.views.generic import ListView

new_todo = {}


def to_do(request,title ):
    '''
    issue: multiple todos
    '''
    todo = get_object_or_404(ToDoItem,title=title)

    return render(request, 'to_do.html',context={"todo":todo})


def to_do_list(request):
    global new_todo
    items = ToDoItem.objects.all()

    if request.method == 'POST':
        
        print(request.POST)
        new_todo = dict(request.POST)

        ToDoItem.objects.create(
            title=new_todo['title'][0],
            datetime=new_todo['datetime'][0],
            location=new_todo['location'][0],
            describtion=new_todo['describtion'][0])

    return render(request,template_name="to_do_list.html",context={"to_dos":items})

def new_todo(request):

    if request.method == 'POST':
        print(request.POST)

    return render(request,'new_todo.html')