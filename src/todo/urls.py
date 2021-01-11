from django.urls import path
from .views import home,todo_list


from .views import home
urlpatterns = [
    path("", home, name='home' ),
    path("list/", todo_list, name='todo-list' )
]


