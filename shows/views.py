from django.shortcuts import render, redirect
from shows.models import Show

from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from datetime import datetime

def all_products(request):
    """ A view to return all shows - include """

    # returns just upcoming dates
    shows = Show.objects.all().filter(date__gte=datetime.now())

    context = {
        'shows': shows
    }

    template = 'shows/shows.html'

    return render(request, template, context)