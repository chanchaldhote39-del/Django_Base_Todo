from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required


# ak task hai uski req post pver jail ani obj create krn task ki and return dirct home
# yaha hum create ker rhe  

@login_required
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


# yaha id alreaady hai ager d hogin to mark_as_done kro nhito 404 msg dedo
def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')
   

def mark_as_UnDone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect("home")


def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')


def delete_UnDone_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')

def edit_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method == "POST":
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    
    else:
        context = {
            'get_task' : get_task,
        }
        return render(request,'edit_task.html',context)
    


# Authentication

@login_required
def home(request):
    tasks = Task.objects.filter(is_completed=False)
    completed_task = Task.objects.filter(is_completed=True)
    context = {
         'tasks': tasks,
        'completed_task': completed_task,
    }
    return render(request, 'home.html', context)


def register_view(request):
    if request.method == 'POST':                               
         form = UserCreationForm(request.POST)                 
         if form.is_valid():                                    
             user = form.save()                                
             login(request, user)                              
             return redirect('home')                      
    else:                                                     
         form = UserCreationForm()                            
    return render(request, 'register.html', {'form': form})


def login_view(request):                                      
    if request.method == 'POST':                              
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():                                  
            user = form.get_user()                           
            login(request, user)                              
            return redirect('home')                         
    else:                                                     
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')