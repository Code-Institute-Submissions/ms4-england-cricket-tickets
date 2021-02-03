from django.shortcuts import render, redirect


# Create your views here.
def view_cart(request):
    """
    A view that renders the cart contents page
    """
    return render(request, 'cart/cart.html',)


def add_to_cart(request, ticket_id):
    """Add a quantity to the shopping cart"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if ticket_id in list(cart.keys()):
        cart[ticket_id] += quantity
    else:
        cart[ticket_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)

