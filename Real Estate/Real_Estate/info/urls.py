from django.urls import path
from info.views import contact

urlpatterns = [
    path('contact/', contact, name='contact'),
]
