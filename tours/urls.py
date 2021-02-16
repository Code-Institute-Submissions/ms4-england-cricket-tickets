from django.urls import path
from . import views

urlpatterns = [
    path('', views.tours, name='tours'),
    path('<int:match_id>/', views.tickets, name='tickets'),
    path('product_management/', views.product_management, name='product_management'),
    path('add_match/', views.add_match, name='add_match'),
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('add_stadium/', views.add_stadium, name='add_stadium'),
    path('add_tour/', views.add_tour, name='add_tour'),
    path('edit_match/<int:match_id>/', views.edit_match, name='edit_match'),
]
