from django.forms import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from .models import TODOList
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def home_page(request):
    if request.method == 'POST':
        done = request.POST.get('done')
        task = request.POST.get('task')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        data = TODOList.objects.create(done=done, task=task, due_date=due_date, priority=priority)
        data.save()
        return redirect('main_page')
    else:
        return render(request, 'TODO_app/home.html')

def main_page(request):
    if request.method in ['POST', 'GET']:
        results = TODOList.objects.all()

    return render(request, 'TODO_app/main.html', context={"results": results})

def edit_task(request, task_id):
    task = get_object_or_404(TODOList, pk=task_id)

    if request.method == 'POST':
        # Handle the form submission and update the task here
        task.done = request.POST.get('done') == 'on'
        task.task = request.POST.get('task')

        due_date_str = request.POST.get('due_date')
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
                task.due_date = due_date
            except ValueError:
                raise ValidationError("Invalid date format")

        task.priority = request.POST.get('priority')
        task.save()
        return redirect('main_page')

    # Check if task.due_date is None or an empty string and set it to a default value
    if not task.due_date:
        task.due_date = datetime.now().date()

    return render(request, 'TODO_app/edit_task.html', {'task': task})


def delete_task(request, task_id):

    if request.method in ['POST', 'GET']:
        data = TODOList.objects.filter(id=task_id)
        data.delete()
        return redirect('main_page')

    return render(request, 'TODO_app/main.html')