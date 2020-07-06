from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm




def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})



def vk(request):
    return render(request, 'main/vk.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'ФОРМА БЫЛА НЕВЕРНОЙ!!'

    form = TaskForm()
    context = {
    'form': form
    }
    return render(request, 'main/create.html', context)
