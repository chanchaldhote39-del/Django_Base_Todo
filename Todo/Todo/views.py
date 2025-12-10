from django.shortcuts import render
from todoapp.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False)
    context = {
        'tasks' : tasks,
    }
    return render(request, 'home.html', context)