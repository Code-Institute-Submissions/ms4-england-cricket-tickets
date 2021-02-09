from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from tours.models import Ticket


# Create your views here.
def view_cart(request):
    """
    A view that renders the cart contents page
    """

    return render(request, 'cart/cart.html',)


def add_to_cart(request, item_id):
    """Add a quantity to the shopping cart"""
    ticket = get_object_or_404(Ticket, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    day = None
    if 'day' in request.POST:
        day = request.POST['day']

    cart = request.session.get('cart', {})

    if day:
        if item_id in list(cart.keys()):
            if day in cart[item_id]['items_by_day'].keys():
                cart[item_id]['items_by_day'][day] += quantity
                messages.success(request, f'Update: {cart[item_id]["items_by_day"][day]} x Day {day} {ticket.friendly_name} tickets now in your cart')
            else:
                cart[item_id]['items_by_day'][day] = quantity
                messages.success(request, f'Added {quantity} x Day {day} {ticket.friendly_name} to your cart')
        else:
            cart[item_id] = {'items_by_day': {day: quantity}}
            messages.success(request, f'Added {quantity} x Day {day} {ticket.friendly_name} to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Update: {cart[item_id]} x {ticket.friendly_name} tickets now in your cart')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {quantity} x {ticket.friendly_name} to your cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):

    """Adjust the quantity of the specified product to the specified amount"""
    ticket = get_object_or_404(Ticket, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    day = None
    if 'day' in request.POST:
        day = request.POST['day']
    cart = request.session.get('cart', {})

    if day:
        if quantity > 0:
            cart[item_id]['items_by_day'][day] = quantity
            messages.success(request, f'Update: {cart[item_id]["items_by_day"][day]} x Day {day} {ticket.friendly_name} tickets now in your cart')

        else:
            del cart[item_id]['items_by_day'][day]
            if not cart[item_id]['items_by_day']:
                cart.pop(item_id)
            messages.success(request, f'Removed {quantity} x Day {day} {ticket.friendly_name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Update: {cart[item_id]} x {ticket.friendly_name} tickets now in your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {ticket.friendly_name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_item(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        ticket = get_object_or_404(Ticket, pk=item_id)
        day = None
        if 'day' in request.POST:
            day = request.POST['day']
        cart = request.session.get('cart', {})

        if day:
            del cart[item_id]['items_by_day'][day]
            if not cart[item_id]['items_by_day']:
                cart.pop(item_id)
            messages.success(request, f'Removed Day {day} {ticket.friendly_name} tickets from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {ticket.friendly_name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)










