from django.urls import path

from to_do.views import to_do, new_todo, to_do_list, delete_todo
from django.urls import path, include

urlpatterns = [
    path("/", to_do_list),
    path("/new", new_todo),
    path("/todo/<str:title>/", to_do),
    path("/todo/<str:title>/delete/",delete_todo)
]