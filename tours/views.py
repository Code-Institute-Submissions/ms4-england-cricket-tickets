from django.shortcuts import render, get_object_or_404
from .models import Tour, Match, Stadium, Ticket

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
