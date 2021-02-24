from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from tours.models import Ticket, Match, Gametype


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            ticket = get_object_or_404(Ticket, pk=item_id)
            total += item_data * ticket.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'ticket': ticket,

            })
        else:
            ticket = get_object_or_404(Ticket, pk=item_id)
            for day, quantity in item_data['items_by_day'].items():
                total += quantity * ticket.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'ticket': ticket,
                    'day': day
                })

    if total > 100:
        delivery = 5
    else:
        delivery = total * Decimal(settings.DELIVERY_CHARGE / 100)

    discount = total * Decimal(settings.MEMBER_DISCOUNT / 100)

    if request.user.is_authenticated:
        grand_total = total - discount + delivery

    else:
        grand_total = total + delivery

    gametype = Gametype.objects.all()
    match = Match.objects.all()

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'discount': discount,
        'grand_total': grand_total,
        'match': match,
        'gametype': gametype
    }

    return context
