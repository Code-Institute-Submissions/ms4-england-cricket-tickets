from django.shortcuts import render
from tours.models import Tour
# Create your views here.


def index(request):
    """ A view to return the index page """

    tours = Tour.objects.all()

    if request.GET:
        if 'tour' in request.GET:
            all_tours = Tour.objects.all()
            tour = request.GET['tour']
            tours = all_tours.filter(name=tour)

    context = {
        'tours': tours
    }

    return render(request, 'home/index.html', context)
