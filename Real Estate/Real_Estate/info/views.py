from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, render_to_response


# Create your views here.
from django.template import RequestContext


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


def handler404(request, *args, **argv):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
