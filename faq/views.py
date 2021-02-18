from django.shortcuts import render
from .models import FAQ

# Create your views here.


def faq(request):
    """
    A view to return the tickets page, showing the
    stadium and tickets available
    """

    faq = FAQ.objects.all()

    context = {
        'faq': faq
    }

    return render(request, 'faq/faq.html', context)
