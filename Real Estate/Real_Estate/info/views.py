from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect


# Create your views here.


def contact(request):
    return render(request, 'contact.html')


def handleEnquiry(request):
    fullname = request.POST['fullname']
    subject = request.POST['subject']
    message = request.POST['message']
    email = request.POST['email']
    send_mail(
        'Subject : ' + subject,
        'Message : ' + message + '\nEnquiry by : ' + fullname,
        email,
        ['sanyam.gupta@tothenew.com'],
        fail_silently=False,
    )
    messages.success(request, f"Hey {fullname}! Your enquiry has been received. We'll contact you ASAP!")
    return redirect("contact")
