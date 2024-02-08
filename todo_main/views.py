
from django.shortcuts import render

from todo.models import Task


def home(request):
    incompletedTasks = Task.objects.filter(is_completed=False)
    completedTasks = Task.objects.filter(is_completed=True)
    context ={
        "incompletedTasks":incompletedTasks,
        "completedTasks":completedTasks,
    }
    return render(request,'index.html',context=context)