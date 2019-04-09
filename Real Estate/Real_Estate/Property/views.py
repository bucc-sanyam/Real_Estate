from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.models import User
from .forms import PropertyForm
from .models import Properties


class PropertyOperations(LoginRequiredMixin, FormView):
    form_class = PropertyForm
    template_name = 'properties.html'

    def get(self, request):
        if request.user.profile.is_seller:
            return render(self.request, 'properties.html', context={'form': PropertyForm})
        else:
            message = 'You are not a seller, please login with a seller account.'
            header = 'Sorry'
            return render(self.request, template_name='properties.html', context={'message': message, 'header': header})

    def form_valid(self, form):
        form.instance.property_seller_name = self.request.user
        form.save()
        message = 'You have successfully posted a property !'
        return render(self.request, template_name='properties.html', context={'message': message})

    def form_invalid(self, form):
        return render(self.request, template_name='properties.html', context={'form': form})


class UpdateProperty(LoginRequiredMixin, UpdateView):
    model = Properties
    fields = ['property_title', 'property_address', 'property_city', 'property_state', 'property_pin',
              'property_price', 'property_bedroom', 'property_bathroom', 'property_sq_feet', 'property_lot_size',
              'property_garage', 'property_description', 'property_image1', 'property_image2', 'property_image3',
              'property_image4', 'property_image5']
    template_name = 'update_property.html'


class ViewAllProperty(ListView):
    model = Properties
    paginate_by = 2
    template_name = 'property_list.html'


class ViewSpecificProperty(DetailView):
    model = Properties
    template_name = 'property_details.html'


# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Properties
#     success_url = '/'
#
#     def test_func(self):
#         property = self.get_object()
#         if self.request.user == property.property_seller_name:
#             return True
#         return False


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
