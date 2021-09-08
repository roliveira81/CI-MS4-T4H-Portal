from django.shortcuts import render, redirect
from shows.models import Show

from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from datetime import datetime


def index(request):
    """ 
    A view to return index page
    Contact form handler 
    """

    # returns just upcoming dates
    shows = Show.objects.all().filter(date__gte=datetime.now())

    context = {
        'shows': shows
    }

    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST.get('phone', False)
        subject = request.POST['subject']
        message = request.POST['message']        

        message = message + '\r\n Name: ' + name

        if len(phone) > 0:
            message = message + '\r\n Phone: ' + phone

        try:
            send_mail(subject, message, email,
                        [settings.DEFAULT_FROM_EMAIL])
        except BadHeaderError:         
            return HttpResponse('Invalid header found!')
        messages.success(request, (
            f'Thank you for e-Mail, '
            ' your message has been sent! '
            'We will respond to you as soon as possible.'))
        return redirect('home')

    template = 'home/index.html'

    return render(request, template, context)