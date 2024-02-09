
from . import views
from django.urls import path

urlpatterns = [
    #add task
    path('addTask/',views.addTask,name='addTask'),

    #mark done and pending
    path('markTaskDone/<int:pk>/',views.markDone,name='markDone'),
    path('markTaskPending/<int:pk>/',views.markPending,name='markPending'),

    #edit feature
    path('editTask/<int:pk>/',views.editTask,name='editTask'),

]