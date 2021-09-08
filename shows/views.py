from django.shortcuts import render
from shows.models import Show


def all_shows(request):
    """ A view to return all shows - include """

    # returns just upcoming dates
    shows = Show.objects.all()

    context = {
        'shows': shows
    }

    template = 'shows/shows.html'

    return render(request, template, context)
