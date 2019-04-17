from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.shortcuts import render, redirect

from Property.models import Enquiry, Properties
from .forms import *
from .models import Profile, User


def registerUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form_user = profile_form.save(commit=False)
            profile_form_user.user = user
            profile_form.instance.image = request.FILES['image']
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
    data = dict()
    if request.method == 'POST':
        return redirect(update_profile)
    else:
        if request.user.profile.is_seller:
            properties = Properties.objects.filter(property_seller_name_id=request.user.id).order_by(
                '-property_listing_date')
            data['properties'] = properties
            page = request.GET.get('page', 1)
            paginator = Paginator(properties, 2)
            try:
                paginator_pages = paginator.page(page)
            except PageNotAnInteger:
                paginator_pages = paginator.page(1)
            except EmptyPage:
                paginator_pages = paginator.page(paginator.num_pages)
            data['properties'] = paginator_pages
        else:
            enquiries = Enquiry.objects.filter(enquiry_user_id=request.user.id).order_by('-date')
            data['enquiries'] = enquiries
        return render(request, 'accounts/profile.html', data)


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
