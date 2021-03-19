from django.db.models import Prefetch
from rest_framework import generics
from rest_framework.permissions import *

from .serializers import *


# Create your views here.

class TodoListAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Todo_list.objects.all()
    serializer_class = Todo_List_Serializer


class TodoIncompleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = TodoGetSerializer

    def get_queryset(self):
        return Todo_list.objects.all().prefetch_related(
            Prefetch('task', queryset=Tasks.objects.filter(mark=False)))


class TodoCompleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoGetSerializer

    def get_queryset(self):
        return Todo_list.objects.all().prefetch_related(
            Prefetch('task', queryset=Tasks.objects.filter(mark=True)))


class TaskListAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Tasks.objects.all()
    serializer_class = Task_Serializer


from django.shortcuts import render

# Create your views here.
