from django.contrib import admin

from todo.models import Task

class TaskAdmin(admin.ModelAdmin):
    search_fields = ('task',)
    list_display = ('task','is_completed','modified_at')


# Register your models here.
admin.site.register(Task,TaskAdmin)