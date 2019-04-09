from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.models import User
from .forms import PropertyForm
from .models import Properties


class RegisterProperty(LoginRequiredMixin, FormView):
    form_class = PropertyForm
    template_name = 'register_property.html'

    def get(self, request):
        if request.user.profile.is_seller:
            return render(self.request, 'register_property.html', context={'form': PropertyForm})
        else:
            message = 'You are not a seller, please login with a seller account.'
            header = 'Sorry'
            return render(self.request, template_name='register_property.html',
                          context={'message': message, 'header': header})

    def form_valid(self, form):
        form.instance.property_seller_name = self.request.user
        form.save()
        messages.add_message(self.request, messages.INFO, 'You have successfully posted a property !')
        return redirect('list_all_property')

    def form_invalid(self, form):
        return render(self.request, template_name='register_property.html', context={'form': form})


class UpdateProperty(LoginRequiredMixin, ListView):
    model = Properties
    template_name = 'update_property.html'


class UpdatePropertyForm(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Properties
    fields = ['property_title', 'property_address', 'property_city', 'property_state', 'property_pin',
              'property_price', 'property_bedroom', 'property_bathroom', 'property_sq_feet', 'property_lot_size',
              'property_garage', 'property_description', 'property_image1', 'property_image2', 'property_image3',
              'property_image4', 'property_image5']
    template_name = 'update_property_form.html'
    success_url = reverse_lazy('list_all_property')

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.property_seller_name:
            return True
        return False


class ViewAllProperty(ListView):
    model = Properties
    template_name = 'property_list.html'


class ViewSpecificProperty(DetailView):
    model = Properties
    template_name = 'property_details.html'


class DeletePropertyList(LoginRequiredMixin, ListView):
    model = Properties
    template_name = 'delete_property_list.html'


class DeleteProperty(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Properties
    template_name = 'properties_confirm_delete.html'
    success_url = reverse_lazy('list_all_property')

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.property_seller_name:
            return True
        return False


def search_property(request):
    if request.method == 'POST':
        property_to_search = request.POST.get('search')
        try:
            status = Properties.objects.filter(property_title__contains=property_to_search)
            if not status:
                raise Exception
            return render(request, 'search.html', {'property': status})
        except Exception:
            return render(request, 'search.html', {'errors': 'Property Not Found !'})
