from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AddTicketForm
from django.contrib import messages
from .models import Ticket


@login_required()
def homepage(request):
    return render(request, 'homepage.html', context={})


@login_required()
def add_ticket(request):
    if request.method == 'POST':
        form = AddTicketForm(request.POST)
        if form.is_valid():
            form_s = form.save(commit=False)
            form_s.user = request.user
            form_s.save()
            messages.success(request, 'Ticket başarıyla oluşturuldu')
        else:
            messages.error(request, 'Boş alan bırakılamaz')
    else:
        form = AddTicketForm()
    return render(request, 'add_ticket.html', context={
        'form': form
    })

@login_required()
def my_tickets(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-id')
    return render(request, 'my_tickets.html', context={
        'tickets':tickets
    })
