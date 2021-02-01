from django.urls import path
from . import views

urlpatterns = [
    path('', views.tours, name='tours'),
    path('<match_id>', views.tickets, name='tickets'),
]
