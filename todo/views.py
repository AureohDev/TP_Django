from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task
from .forms import AddTaskForm

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

def add(request):
    return HttpResponse('add')

def edit(request, task_id):
    return 'edit'

def done(request, task_id):
    return 'done'

def delete(request, task_id):
    return 'delete'