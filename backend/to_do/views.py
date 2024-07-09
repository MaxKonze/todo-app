from django.shortcuts import render
from django.http import HttpResponse


def to_dos(request):
    return render(request, 'to_do_list.html')