from django.urls import path
from .views import homepage, add_ticket, my_tickets

urlpatterns = [
    path('', homepage, name='homepage'),
    path('add-ticket/', add_ticket, name='add_ticket'),
    path('my-tickets/', my_tickets, name='my_tickets')
]