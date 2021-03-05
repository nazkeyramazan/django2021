from django.shortcuts import render
from main.models import Tasks , Todo_list
# Create your views here.
def todo_list_all(request):
    list = Todo_list.objects.all();
    context = { 'list' : list};
    return render(request , 'list.html' , context )

def todo_list(request , pk):
    task = Tasks.objects.filter(todos_id=pk, mark=False)
    list = Todo_list.objects.get(id = pk)

    context = {
        'tasks': task,
        'list':list,
    }
    return render(request , 'todo_list.html' , context)


def completed_todo_list(request , pk):
    task = Tasks.objects.filter(todos=pk , mark = True)
    list = Todo_list.objects.get(id = pk);
    context = {
        'tasks':task ,
        'list' : list
               }
    return render(request , 'completed_todo_list.html' , context)