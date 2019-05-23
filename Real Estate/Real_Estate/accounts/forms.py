import re

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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(u'This email address is already registered.')
        return email


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

    def clean(self):
        cd = self.cleaned_data
        patter_number = re.compile("^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$")
        if not re.match(patter_number, str(cd.get("phone_number"))):
            self.add_error('phone_number', "The phone number must be in Indian Format.")
        return cd


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'description', 'image']

    def clean(self):
        cd = self.cleaned_data
        patter_number = re.compile("^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$")
        if not re.match(patter_number, str(cd.get("phone_number"))):
            self.add_error('phone_number', "The phone number must be in Indian Format.")
        return cd
