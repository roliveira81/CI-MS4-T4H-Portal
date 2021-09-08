from django.shortcuts import render
from shows.models import Show

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
