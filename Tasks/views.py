from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def show_list(request):
    tasks = Task.objects.all() 
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')  
        Task.objects.create(title=title)
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
