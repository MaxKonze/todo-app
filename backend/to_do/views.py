from django.shortcuts import render
from django.http import HttpResponse

output = ''


def to_dos(request):
    global output

    if request.method == 'POST':
        output = (request.POST['new_task'])
        print(output)

    return render(request, 'to_do_list.html')