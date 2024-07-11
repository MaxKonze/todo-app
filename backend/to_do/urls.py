from django.urls import path

from to_do.views import to_dos, new_todo
from django.urls import path, include

urlpatterns = [
    path("/", to_dos),
    path("/new", new_todo)
]