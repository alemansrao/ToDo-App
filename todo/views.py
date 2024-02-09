from django.http import HttpResponse
from django.shortcuts import redirect, render

from todo.models import Task

# Create your views here.

def addTask(request):
    taskString = request.POST.get('task')
    Task.objects.create(task=taskString)
    # Task.save()

    return redirect("home")