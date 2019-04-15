from django.urls import path
from info.views import contact, handleEnquiry

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('contact/enquiry/', handleEnquiry, name="handleEnquiry")
]
