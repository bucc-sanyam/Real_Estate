from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.models import User
from .forms import PropertyForm
from .models import Properties, Enquiry


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
    ordering = ['-property_listing_date']

    def get_context_data(self, **kwargs):
        context = super(UpdateProperty, self).get_context_data(**kwargs)
        properties = Properties.objects.filter(property_seller_name_id=self.request.user.id).order_by(
            '-property_listing_date')
        context['properties'] = properties
        return context


class UpdatePropertyForm(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Properties
    form_class = PropertyForm
    template_name = 'update_property_form.html'
    success_url = reverse_lazy('list_all_property')

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.property_seller_name:
            return True
        return False

    def handle_no_permission(self):
        return render(self.request, 'access_denied.html')


class ViewAllProperty(ListView):
    model = Properties
    template_name = 'property_list.html'
    paginate_by = 3
    ordering = ['-property_listing_date']


class MyPropertyList(ListView):
    model = Properties
    template_name = 'my_property_list.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(MyPropertyList, self).get_context_data(**kwargs)
        properties = Properties.objects.filter(property_seller_name_id=self.request.user.id).order_by(
            '-property_listing_date')
        context['properties'] = properties
        return context


class ViewSpecificProperty(DetailView):
    model = Properties
    template_name = 'property_details.html'

    def get_context_data(self, **kwargs):
        context = super(ViewSpecificProperty, self).get_context_data(**kwargs)
        enquiries = Enquiry.objects.filter(property=kwargs['object'].id)
        context['enquiries'] = enquiries
        for enquiry in enquiries:
            if self.request.user.id == enquiry.enquiry_user.id:
                context['enquiry_made'] = True
                break
        return context


class DeletePropertyList(LoginRequiredMixin, ListView):
    model = Properties
    template_name = 'delete_property_list.html'
    ordering = ['-property_listing_date']

    def get_context_data(self, **kwargs):
        context = super(DeletePropertyList, self).get_context_data(**kwargs)
        properties = Properties.objects.filter(property_seller_name_id=self.request.user.id).order_by(
            '-property_listing_date')
        context['properties'] = properties
        return context


class DeleteProperty(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Properties
    template_name = 'properties_confirm_delete.html'
    success_url = reverse_lazy('list_all_property')

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.property_seller_name:
            return True
        return False

    def handle_no_permission(self):
        return render(self.request, 'access_denied.html')


def access(request):
    return render(request, "access_denied.html")


def handlequery(request, id):
    new_enquiry = Enquiry()
    new_enquiry.enquiry_user = User.objects.get(id=request.user.id)
    name = new_enquiry.property = Properties.objects.get(id=id)
    description = new_enquiry.description = request.POST['description']
    new_enquiry.save()
    send_mail(
        'Enquiry for ' + name.property_title,
        'Enquiry by : ' + request.user.first_name + ' ' + request.user.last_name +
        '\nEnquiry : ' + description,
        request.user.email,
        [name.property_seller_name.email],
        fail_silently=False,
    )
    return redirect("list_all_property")


def home(request):
    data = dict()
    if request.method == 'POST':
        invalid_entries = [' ', '', ""]
        if request.POST.get('select-city') is None or 'All Cities':
            city_search_results = Properties.objects.all()
        else:
            city_search_results = Properties.objects.filter(property_city=request.POST.get('select_city', ""))
        if request.POST.get('select-state') is None or 'All States':
            state_search_results = Properties.objects.all()
        else:
            state_search_results = Properties.objects.filter(property_states=request.POST.get('select_state', ""))
        query_result = city_search_results
        query_result = query_result.union(state_search_results)
        if request.POST.get('property-name') not in invalid_entries:
            print('here')
            text_search_results = Properties.objects.filter(
                property_title__icontains=request.POST.get('property-name'))
            query_result = query_result.intersection(text_search_results)
        data['object_list'] = query_result
        data['search'] = 'Search Results'
        return render(request, 'property_list.html', data)
    else:
        form = PropertyForm
        properties = []
        i = 0
        property_list = Properties.objects.filter().order_by('-property_listing_date')
        for property in property_list:
            if i < 3:
                properties.append(property)
            i = i + 1
        data['properties'] = properties
        data['form'] = form
        return render(request, "home.html", data)
