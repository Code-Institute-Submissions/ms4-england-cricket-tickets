from django.shortcuts import render, redirect, reverse, HttpResponse


# Create your views here.
def view_cart(request):
    """
    A view that renders the cart contents page
    """

    return render(request, 'cart/cart.html',)


def add_to_cart(request, item_id):
    """Add a quantity to the shopping cart"""
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
            else:
                cart[item_id]['items_by_day'][day] = quantity
        else:
            cart[item_id] = {'items_by_day': {day: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)
    

def update_cart(request, item_id):
    """Update the quantity in the shopping cart"""
    quantity = int(request.POST.get('quantity'))   
    day = None
    if 'day' in request.POST:
        day = request.POST['day']
    cart = request.session.get('cart', {})

    if day:
        if quantity > 0:
            cart[item_id]['items_by_day'][day] = quantity
        else:
            del cart[item_id]['items_by_day'][day]
            if not cart[item_id]['items_by_day']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_item(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        day = None
        if 'day' in request.POST:
            day = request.POST['day']
        cart = request.session.get('cart', {})

        if day:
            del cart[item_id]['items_by_day'][day]
            if not cart[item_id]['items_by_day']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)







