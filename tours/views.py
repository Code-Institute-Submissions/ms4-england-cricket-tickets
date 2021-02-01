from django.shortcuts import render
from .models import Tour, Match

# Create your views here.

def tours(request):
    """ A view to return the tours page, including sorting and search queries """

    tours = Tour.objects.all()
    matches = Match.objects.all()

    context = {
        'tours': tours,
        'matches': matches
    }

    return render(request, 'tours/tours.html', context)
