from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Tour, Match, Stadium, Ticket

# Create your views here.

def tours(request):
    """ A view to return the tours page, including sorting and search queries """

    tours = Tour.objects.all()
    matches = Match.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You haven't searched for anything, please try again!")
                return redirect(reverse('tours'))

            queries = Q(name__icontains=query)
            tours = tours.filter(queries)

    context = {
        'tours': tours,
        'matches': matches,
        'search_term': query
    }

    return render(request, 'tours/tours.html', context)


def tickets(request, match_id):
    """
    A view to return the tickets page, showing the
    stadium and tickets available
    """

    match = get_object_or_404(Match, pk=match_id)
    stadiums = Stadium.objects.all()
    tickets = Ticket.objects.all()

    context = {
        'match': match,
        'stadiums': stadiums,
        'tickets': tickets
    }

    return render(request, 'tours/tickets.html', context)
