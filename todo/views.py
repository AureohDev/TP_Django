from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Task
from .forms import AddTaskForm, EditTaskForm

# Create your views here.

def index(request):
    tasks_list = Task.objects.all() 
    template = loader.get_template('todo/index.html')
    context = {
        'tasks_list': tasks_list
    }

    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form_content= form.cleaned_data['content']

            content = Task.objects.filter(content=form_content)
            if not content.exists():
                content = Task.objects.create(
                    content=form_content,
                    is_done=False
                )       
    else: 
        form = AddTaskForm()  

    context['form'] = form
    return HttpResponse(template.render(context, request))


def edit(request, task_id):
    task = Task.objects.get(pk=task_id)
    template = loader.get_template('todo/edit.html') 
    context = {
        'task': task
    }

    if request.method == 'POST':
        form = EditTaskForm(request.POST)
        if form.is_valid():
            form_content = form.cleaned_data['content']
            form_is_done = form.cleaned_data['is_done']

            task.content = form_content
            task.is_done = form_is_done
            task.save()
    else: 
        form = EditTaskForm(initial={'content': task.content,'is_done':task.is_done})  

    context['form'] = form
    return HttpResponse(template.render(context, request))

def done(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_done = True
    task.save()
    return redirect('index')

def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('index')