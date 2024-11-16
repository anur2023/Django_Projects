from django.shortcuts import redirect, render
from .models import Members
from .form import Memberform
from django.contrib import messages
# Create your views here.
def home(request):
    all_member = Members.objects.all
    return render(request,'home.html',{'all':all_member})

def join(request):
    if request.method == 'POST':
        form = Memberform(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('Your form has been submitted successfully!'))
        return redirect('home')
    else:
        return render(request,'join.html',{})

