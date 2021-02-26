from django.shortcuts import render
tasks =[{
        'task': 'Task 1',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': True
    },
        {'task': 'Task 2',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': True
    },
        {'task': 'Task 3',
         'created': '10/09/2018',
         'due_on': '12/09/2018',
         'owner': 'admin',
         'mark': True
         },
        {'task': 'Task 4',
         'created': '10/09/2018',
         'due_on': '12/09/2018',
         'owner': 'admin',
         'mark': True
         },
        {'task': 'Task 0',
         'created': '10/09/2018',
         'due_on': '12/09/2018',
         'owner': 'admin',
         'mark': False
         },
    ]
# Create your views here.
def todo_list(request):
    return render(request, 'todo_list.html' , {'context': tasks})

def comleted_todo_list(request):
    return render(request , 'completed_todo_list.html' , {'context': tasks} )