from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    creator = {
        'title': 'About',
        'Name': 'Sanyam Gupta',
        'Number': '9999164691',
        'Profile': 'Trainee',
        'email': 'sanyamgupta@tothenew.com'
    }
    return render(request, 'about.html', creator)

