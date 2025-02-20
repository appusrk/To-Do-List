from django.shortcuts import render, redirect
from .models import Task, Reg
from datetime import datetime

# Create your views here.)
def home(request):
    return render(request, 'tasks/home.html')

def sign(request):
    if request.method == 'POST':
        name = request.POST.get('name')  
        passw = request.POST.get('passw')  
        email = request.POST.get('email')
        if name and passw and email:  # Ensure no empty values are submitted
            Reg.objects.create(name=name, passw=passw, email=email)
            return redirect('task_list')
        else:
            pass  
    return render(request, 'tasks/signup.html')  

def show_list(request):
    query = request.GET.get('q')
    if query:
        tasks = Task.objects.filter(title__icontains=query)
    else:
        tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')  
        task_date = request.POST.get("date")  
        task_time = request.POST.get("time")
        Task.objects.create(title=title, due_date=task_date, ontime=task_time)
        return redirect('task_list')  
    return render(request, 'tasks/add_list.html')  

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id) 
    task.completed = True  
    task.save()  
    return redirect('task_list')  
