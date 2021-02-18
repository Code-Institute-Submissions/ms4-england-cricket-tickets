from django.shortcuts import render
from .models import FAQ
from tours.models import Tour
# Create your views here.


def faq(request):
    """
    A view to return the FAQ page
    """

    faq = FAQ.objects.all()
    tours = Tour.objects.all()

    if request.GET:
        if 'tour' in request.GET:
            all_tours = Tour.objects.all()
            tour = request.GET['tour']
            tours = all_tours.filter(name=tour)

    context = {
        'faq': faq,
        'tours': tours
    }

    return render(request, 'faq/faq.html', context)
