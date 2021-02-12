from django.urls import path
from . import views

urlpatterns = [
    path('', views.tours, name='tours'),
    path('<int:match_id>/', views.tickets, name='tickets'),
    path('add/', views.add_match, name='add_match'),
]
