from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

@login_required
def home(request):
    template_name = 'home.html'
    return render(request, template_name, {})


@login_required
def update(request):
    template_name = 'registration/update.html'
    if request.user.is_authenticated:
        user = request.user
        form = UpdateForm(request.POST, instance = user)
        if request.method == "POST":   
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.instance)
                return redirect('/')
            else: 
                return render(request, 'update.html', {'form': form})
        else: 
            form = UpdateForm(instance = user)
        return render(request, template_name, {'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('app:home')
    else:
        template_name = 'registration/register.html'
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'Your account has been created. You can log in now!')
                return redirect('login')
        else:
            form = UserRegistrationForm()

        context = {'form': form}
        return render(request, template_name, context)
    
@login_required
def log_out(request):
    logout(request)
    return redirect('login')