from django.urls import include, path

from to_do.views import delete_todo, edit_todo, new_todo, to_do, to_do_list

urlpatterns = [
    path("/", to_do_list),
    path("/new", new_todo),
    path("/todo/<str:title>/", to_do),
    path("/todo/<str:title>/delete/", delete_todo),
    path("/todo/<str:title>/edit/", edit_todo),
]
