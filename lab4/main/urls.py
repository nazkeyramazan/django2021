from django.contrib import admin
from django.urls import path
from .views import todo_list , completed_todo_list , todo_list_all

urlpatterns = [
    path( ''  , todo_list_all , name = 'todo_list_all' ),
    path( '<int:pk>/' , todo_list , name = 'todo_list' ),
    path('<int:pk>/completed/',  completed_todo_list, name='completed_todo_list'),
]
