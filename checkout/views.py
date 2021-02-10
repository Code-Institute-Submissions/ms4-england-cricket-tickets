from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There are no tickets in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I971gA47CKnR81lZ8bFTi3WXS6vd3fNrdFEH0Ej90OTpSqolFeXz0Tlvb14ynYO8HJ5kQdjLMBxP8U3SdMcOuGH00cfLPz2mg',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)