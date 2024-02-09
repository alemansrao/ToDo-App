from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from todo.models import Task

# Create your views here.

def addTask(request):
    taskString = request.POST.get('task')
    if taskString != '':
        Task.objects.create(task=taskString)
        return redirect("home")

def markDone(request,pk):
    task = Task.objects.filter(pk=pk).update(is_completed=True)
    # return HttpResponse(pk)
    return redirect("home")
def markPending(request,pk):
    task = Task.objects.filter(pk=pk).update(is_completed=False)
    return redirect("home")


def editTask(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if(request.method == 'POST'):
        taskString = request.POST.get('task')
        task = Task.objects.filter(pk=pk).update(task=taskString)
        # return HttpResponse(taskString)
        return redirect("home")
    else:
        context = {
            "pk":pk,
            "task":task,
            }
        return render(request,"editTask.html",context=context)
