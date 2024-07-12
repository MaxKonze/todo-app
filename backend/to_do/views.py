from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ToDoItem

del_item = None


def to_do(request,title ): 
    '''
     Renders the to-do item detail page based on the provided title
    
    Parameters:    
        request (HttpRequest): The HTTP request object 
        title (str): The title of the to-do item to be retrieved    
    
    Returns:    
        HttpResponse: The rendered todo page
    '''

    global del_item
    todo = get_object_or_404(ToDoItem,title=title)
    del_item = None

    return render(request, 'to_do.html',context={"todo":todo})


def to_do_list(request):
    '''
    Handles the display and creation of to-do items.

    POST request:
        Creates a new to-do item if the todo has a unique name

    Parameters:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: The rendered todo list page
    '''

    global del_item
    new_todo = {}
    items = ToDoItem.objects.all()

    if request.method == 'POST':
        
        print(request.POST)
        new_todo = dict(request.POST)


        try:
            for item in items:
                if item.title == new_todo['title'][0]:
                    return render(request,template_name="to_do_list.html",context={"to_dos":items})

            ToDoItem.objects.create(
                title=new_todo['title'][0],
                datetime=new_todo['datetime'][0],
                location=new_todo['location'][0],
                description=new_todo['description'][0])
            
        except KeyError:
            pass
    
    items = ToDoItem.objects.all()
    return render(request,template_name="to_do_list.html",context={"to_dos":items})

def new_todo(request):
    '''
    Handles the display of the form for a new todo

    Parameters:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: The rendered new todo page
    '''

    return render(request,'new_todo.html')

def delete_todo(request,title):
    global del_item

    del_item = ToDoItem.objects.filter(title=title).delete()

    return redirect("/to_do/")