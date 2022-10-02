from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']