from django.shortcuts import render, redirect


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
        else: cart[item_id] = {'items_by_day': {day: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    
    return redirect(redirect_url)

