from django.urls import path
from .views import homepage, add_ticket

urlpatterns = [
    path('', homepage, name='homepage'),
    path('add-ticket/', add_ticket, name='add_ticket')
]