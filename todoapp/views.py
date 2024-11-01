from django .shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from todoapp import models
from todoapp.models import Todoo
from django.contrib.auth import  authenticate,login as auth_login,logout
def signup(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        email_id = request.POST.get('email')
        pwd = request.POST.get('password')
        print(user_name,email_id,pwd)
        my_user = User.objects.create_user(user_name,email_id,pwd)
        my_user.save()
        return redirect('/login')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pwd = request.POST.get('password')
        print(user_name,pwd)
        users = authenticate(request, username =user_name,password = pwd )
        if users is not None:
            auth_login(request,users)
            return redirect('/todo')
        else:
            return redirect('/login')

    return render(request,'login.html')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        srno = request.POST.get('srno')

        if srno:  # Check if srno is provided for editing
            todo = get_object_or_404(Todoo, srno=srno, user=request.user)
            todo.title = title
            todo.save()
        else:  # Create a new To-Do item
            obj = models.Todoo(title=title, user=request.user)
            obj.save()

        return redirect('Todo')  # Redirect using the name defined in urls.py

    # Fetch all To-Do items for the logged-in user
    todos = models.Todoo.objects.filter(user=request.user).order_by('-date')

    return render(request, 'todo.html', {'todos': todos})


def edit_todo(request, srno):
    todo = get_object_or_404(models.Todoo, srno=srno, user=request.user)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.save()
        return redirect('Todo')  # Redirect by name
    return render(request, 'todo.html', {'todo': todo, 'todos': models.Todoo.objects.filter(user=request.user).order_by('-date')})

def delete_todo(request, srno):
    todo = get_object_or_404(models.Todoo, srno=srno, user=request.user)
    todo.delete()
    return redirect('Todo')  # Redirect by name
    