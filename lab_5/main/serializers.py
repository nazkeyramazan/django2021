from rest_framework import serializers
from .models import *


class Todo_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Todo_list
        fields = '__all__'


class Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'task', 'created_date', 'due_on', 'owner', 'mark', 'todos')


class TodoGetSerializer(serializers.ModelSerializer):
    task = Task_Serializer(many=True, read_only=True)

    class Meta:
        model = Todo_list
        fields = ('id', 'name' , 'task')