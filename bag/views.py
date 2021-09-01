from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to render that products purchased page """

    return render(request, 'bag/bag.html')