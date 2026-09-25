from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def Index(request):
    context = {"message":"Discover visual stories, landscape views, and creative moments."}
    return render(request, "landing/index.html", context)



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the user after signup
            return redirect('/')
    else:
        form = UserCreationForm()
    
    return render(request, 'landing/register.html', {'form': form})
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'landing/login.html', {'form': form})