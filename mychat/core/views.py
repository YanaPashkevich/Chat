from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import SingUpForm


def index(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':
        sign_up_form = SingUpForm(request.POST)

        if sign_up_form.is_valid():
            user = sign_up_form.save()

            login(request, user)

            return redirect('index')
    else:
        sign_up_form = SingUpForm()
        
    return render(request, 'sign_up.html', {'sign_up_form':sign_up_form})