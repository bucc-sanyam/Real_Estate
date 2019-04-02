from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm


def registerUser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")

    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
