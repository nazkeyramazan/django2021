from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('', views.TodoListAPIView.as_view()),
    path('<int:pk>/', views.TodoIncompleteRetrieveAPIView.as_view()),
    path('<int:pk>/completed/', views.TodoCompleteRetrieveAPIView.as_view()),
    path('tasks/', views.TaskListAPIView.as_view())
]