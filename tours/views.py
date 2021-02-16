from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Tour, Match, Stadium, Ticket, Gametype
from .forms import MatchForm
# Create your views here.

def tours(request):
    """ A view to return the tours page, including sorting and search queries """

    tours = Tour.objects.all()
    matches = Match.objects.all()
    gametypes = Gametype.objects.all()
    stadiums = Stadium.objects.all()
    tour = None
    query = None
    stadium = None

    if request.GET:
        if 'tour' in request.GET:
            all_tours = Tour.objects.all()
            tour = request.GET['tour']
            tours = all_tours.filter(name=tour)

        if 'stadium' in request.GET:
            all_stadiums = Stadium.objects.all()
            stadium = request.GET['stadium']
            stadiums = all_stadiums.filter(match__stadium__name__icontains=stadium)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You haven't searched for anything, please try again!")
                return redirect(reverse('tours'))

            queries = Q(name__icontains=query)|Q(match__stadium__name__icontains=query)
            tours = tours.filter(queries)

    context = {
        'tours': tours,
        'matches': matches,
        'gametypes': gametypes,
        'stadiums': stadiums,
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
    tours = Tour.objects.all()

    context = {
        'match': match,
        'stadiums': stadiums,
        'tickets': tickets,
        'tours': tours
    }

    return render(request, 'tours/tickets.html', context)

def add_match(request):
    """Add a match to the store"""
    if request.method == "POST":
        form = MatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added match!')
            return redirect(reverse('add_match'))
        else:
                messages.error(request, 'Failed to add match. Please ensure the form is valid.')
    else:
        form = MatchForm()
    
    template = 'tours/add_match.html'
    context = {
        'form': form,

    }
    return render(request, template, context)
