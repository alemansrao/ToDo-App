from django.http import HttpResponse
from django.shortcuts import redirect, render

from todo.models import Task

# Create your views here.

def addTask(request):
    taskString = request.POST.get('task')
    if taskString != '':
        Task.objects.create(task=taskString)
        return redirect("home")