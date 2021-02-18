from django.shortcuts import render
from .models import FAQ

# Create your views here.


def faq(request):
    """
    A view to return the FAQ page
    """

    faq = FAQ.objects.all()

    context = {
        'faq': faq
    }

    return render(request, 'faq/faq.html', context)
