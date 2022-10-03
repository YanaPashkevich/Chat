from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from core.forms import SingUpForm




@login_required
def profile(request):
    if request.method == "POST":
        sign_up_form = SingUpForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if sign_up_form.is_valid() and profile_form.is_valid():
            sign_up_form.save()
            profile_form.save()    

    sign_up_form = SingUpForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    dict['sign_up_form'] = sign_up_form
    dict['profile_form'] = profile_form

    return render(request, 'profile.html', dict)