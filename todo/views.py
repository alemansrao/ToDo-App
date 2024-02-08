from django.http import HttpResponse
from django.shortcuts import render

from todo.models import Task

# Create your views here.

def addTask(request):
    taskString = request.POST.get('task')
    taskObject = Task(task=taskString)
    taskObject.save()
    return HttpResponse(taskString if taskString!=None else "No post request received")