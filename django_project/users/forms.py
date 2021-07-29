from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegisterForm(UserCreationForm):
    email=forms.EmailField() #required=True (default)


    class Meta:
        model=User
        fields=['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField() #required=True (default)


    class Meta:
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):   #This profile form will allow to update the profile pics
    class Meta:
        model=Profile
        fields=['image']


