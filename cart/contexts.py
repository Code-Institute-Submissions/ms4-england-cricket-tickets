from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from tours.models import Ticket


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        ticket = get_object_or_404(Ticket, pk=item_id)
        total += quantity * ticket.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'ticket': ticket,
        })

    delivery = total * Decimal(settings.DELIVERY_CHARGE / 100)

    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
