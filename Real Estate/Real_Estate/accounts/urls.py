from django.urls import path
from accounts.views import registerUser


urlpatterns = [
    path('register/', registerUser, name='register'),
]