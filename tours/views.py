from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Tour, Match, Stadium, Ticket, Gametype
from .forms import MatchForm, TicketForm, StadiumForm, TourForm
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


@login_required
def product_management(request):
    """ A view to return the index page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('tours'))
    
    tours = Tour.objects.all()

    if request.GET:
        if 'tour' in request.GET:
            all_tours = Tour.objects.all()
            tour = request.GET['tour']
            tours = all_tours.filter(name=tour)

    context = {        
        'tours': tours
    }

    return render(request, 'tours/product_management.html', context)


@login_required
def add_match(request):
    """Add a match to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('tours'))

    if request.method == "POST":
        form = MatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added match!')
            return redirect(reverse('tours'))
        else:
            messages.error(request, 'Failed to add match. Please ensure the form is valid.')
    else:
        form = MatchForm()
    
    tours = Tour.objects.all()

    if request.GET:
        if 'tour' in request.GET:
            all_tours = Tour.objects.all()
            tour = request.GET['tour']
            tours = all_tours.filter(name=tour)

    template = 'tours/add_match.html'
    context = {
        'form': form,
        'tours': tours

    }
    return render(request, template, context)

@login_required
def add_ticket(request):
    """Add a ticket to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('tours'))

    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added ticket!')
            return redirect(reverse('add_ticket'))
        else:
            messages.error(request, 'Failed to add ticket. Please ensure the form is valid.')
    else:
        form = TicketForm()

    template = 'tours/add_ticket.html'

    tours = Tour.objects.all()

    if request.GET:
        if 'tour' in request.GET:
            all_tours = Tour.objects.all()
            tour = request.GET['tour']
            tours = all_tours.filter(name=tour)

    context = {
        'form': form,
        'tours': tours

    }
    return render(request, template, context)


@login_required
def add_stadium(request):
    """Add a stadium to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('tours'))

    if request.method == "POST":
        form = StadiumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added stadium!')
            return redirect(reverse('add_stadium'))
        else:
            messages.error(request, 'Failed to add stadium. Please ensure the form is valid.')
    else:
        form = StadiumForm()
    
    tours = Tour.objects.all()

    if request.GET:
        if 'tour' in request.GET:
            all_tours = Tour.objects.all()
            tour = request.GET['tour']
            tours = all_tours.filter(name=tour)

    template = 'tours/add_stadium.html'
    context = {
        'form': form,
        'tours': tours

    }
    return render(request, template, context)


@login_required
def add_tour(request):
    """Add a tour to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('tours'))

    if request.method == "POST":
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added tour!')
            return redirect(reverse('add_tour'))
        else:
            messages.error(request, 'Failed to add tour. Please ensure the form is valid.')
    else:
        form = TourForm()
    
    tours = Tour.objects.all()

    if request.GET:
        if 'tour' in request.GET:
            all_tours = Tour.objects.all()
            tour = request.GET['tour']
            tours = all_tours.filter(name=tour)

    template = 'tours/add_tour.html'
    context = {
        'form': form,
        'tours': tours

    }
    return render(request, template, context)


@login_required
def edit_match(request, match_id):
    """edit a match in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('tours'))

    match = get_object_or_404(Match, pk=match_id)
    if request.method == 'POST':
        form = MatchForm(request.POST, request.FILES, instance=match)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated match!')
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to update match. Please ensure the form is valid.')
    else:
        form = MatchForm(instance=match)
        messages.info(request, f'You are editing {match.name}')
    
    tours = Tour.objects.all()

    if request.GET:
        if 'tour' in request.GET:
            all_tours = Tour.objects.all()
            tour = request.GET['tour']
            tours = all_tours.filter(name=tour)

    template = 'tours/edit_match.html'
    context = {
        'form': form,
        'match': match,
        'tours': tours
    }
    return render(request, template, context)


@login_required
def edit_ticket(request, ticket_id):
    """edit a ticket in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('tours'))

    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated ticket!')
            return redirect(reverse('product_management'))
        else:
            messages.error(request, 'Failed to update ticket. Please ensure the form is valid.')
    else:
        form = TicketForm(instance=ticket)
        messages.info(request, f'You are editing {ticket.friendly_name}')
    
    tours = Tour.objects.all()

    if request.GET:
        if 'tour' in request.GET:
            all_tours = Tour.objects.all()
            tour = request.GET['tour']
            tours = all_tours.filter(name=tour)

    template = 'tours/edit_ticket.html'
    context = {
        'form': form,
        'ticket': ticket,
        'tours': tours
    }
    return render(request, template, context)


@login_required
def delete_match(request, match_id):
    """Delete a match from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('tours'))

    match = get_object_or_404(Match, pk=match_id)
    match.delete()
    messages.success(request, "Match deleted!")
    return redirect(reverse('tours'))


@login_required
def delete_ticket(request, ticket_id):
    """Delete a match from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('tours'))

    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.delete()
    messages.success(request, "Ticket deleted!")
    return redirect(reverse('product_management'))
