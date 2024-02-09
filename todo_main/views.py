
from django.shortcuts import render

from todo.models import Task


def home(request):
    incompletedTasks = Task.objects.filter(is_completed=False).order_by("-modified_at")
    completedTasks = Task.objects.filter(is_completed=True).order_by("-modified_at")
    context ={
        "incompletedTasks":incompletedTasks,
        "completedTasks":completedTasks,
    }
    return render(request,'index.html',context=context)