from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import *
from .models import Profile, User


def registerUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form_user=profile_form.save(commit=False)
            profile_form_user.user = user
            profile_form_user.save()
            name = user_form.cleaned_data.get('first_name')
            messages.success(request, f"Hey {name}! Your account has been created. You can now login!")
            return redirect('login')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form, 'title': "Registration Page"})


@login_required
def profile(request):
    if request.method == 'POST':
        return redirect(update_profile)
    else:
        return render(request, 'accounts/profile.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'accounts/update_profile.html', context)
