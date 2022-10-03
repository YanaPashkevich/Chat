from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ProfileForm, UserForm
from django.contrib.auth.decorators import login_required




@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()    

    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    dict['user_form'] = user_form
    dict['profile_form'] = profile_form

    return render(request, 'profile.html', dict)