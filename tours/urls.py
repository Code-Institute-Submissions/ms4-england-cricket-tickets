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
    path('delete_match/<int:match_id>/', views.delete_match, name='delete_match'),
    path('edit_ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
]
