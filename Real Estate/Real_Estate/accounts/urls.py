from django.urls import path
from accounts.views import registerUser


urlpatterns = [
    path('', registerUser, name='register'),
]