from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Task
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('index')  # Redirect to the homepage or any other page
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'base/profile.html')


@login_required
def index(request):
    context = Task.objects.filter(user=request.user)
    #context.order_by('complete')
    if request.method == 'POST':
        
        title = request.POST['title']
        content = request.POST['content']
        user = request.user
        Task.objects.create(user=user,title=title, content=content)
        return redirect('index')
    return render(request, 'base/index.html', {'tasks':context})

@login_required
def task_content(request, pk):
    content = Task.objects.get(id=pk)
    return render(request, 'base/task_content.html', {'task':content})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        # Update the task with the new data from the form
        task.title = request.POST['title']
        task.content = request.POST['content']
        
        if request.POST['complete'] == 'on':
            task.complete = True
        task.save()

        # Redirect back to the task content page or any other page you prefer
        return redirect('index', pk=pk)

    return render(request, 'base/task_update.html', {'task': task})

@login_required
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('index')
