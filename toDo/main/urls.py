from django.contrib import admin
from django.urls import path
from .views import todo_list , comleted_todo_list

urlpatterns = [
    path('' , todo_list  , name= 'todo_list'),
    path('1/completed/' , comleted_todo_list  , name = 'comleted_todo_list'),
]