
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user, is_completed=False)
    completed_task = Task.objects.filter(user=request.user, is_completed=True)

    return render(request, 'home.html', {
        'tasks': tasks,
        'completed_task': completed_task,
    })


@login_required
def addTask(request):
    if request.method == "POST":
        task = request.POST.get('task')
        if task:
            Task.objects.create(task=task, user=request.user)
    return redirect('home')


@login_required
def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = True
    task.save()
    return redirect('home')

 
@login_required
def mark_as_UnDone(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = False
    task.save()
    return redirect('home')

@login_required
def delete_UnDone_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user, is_completed=True)
    task.delete()
    return redirect('home')


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('home')




@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        task.task = request.POST.get('task')
        task.save()
        return redirect('home')

    return render(request, 'edit_task.html', {'get_task': task})


# -------- AUTH --------

def register_view(request):
   if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
     # if user existes krt asn tr register valy page ver redirect hoil
        user = User.objects.filter(username=username)
    
        if user.exists():
         messages.info(request, 'Username already taken')
         return redirect('/register/')
    
     
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,

             )
        user.set_password(password)
        user.save() # set_password in=build
        messages.info(request, 'Account created successfully')
        return redirect ('/register/')

   return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

        login(request, user)
        return redirect('home')

    return render(request, 'login.html') 


def logout_view(request):
    logout(request)
    return redirect('login')
