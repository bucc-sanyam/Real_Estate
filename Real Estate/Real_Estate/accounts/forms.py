from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
        labels = {
            'password2': 'Confirm Password',
            'first_name': 'First Name',
            'last_name': 'Second Name',
            'email': 'E-Mail'
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'description', 'is_seller', 'image')
        labels = {
            'phone_number': 'Phone',
            'description': 'About',
            'is_seller': 'Account Type',
            'image': 'Profile Picture'
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'description', 'image']
