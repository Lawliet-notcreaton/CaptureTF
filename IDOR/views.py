from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from .forms import *
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import TicketsForm
from .models import Ticket


class DeleteItemView(DeleteView):
    model = Ticket
    success_url = '/tickets.php'
    template_name = 'CTF/lessons/IDOR/delete.php'


# Create your views here.


def lesson1(request):
    return render(request, 'CTF/lessons/IDOR/index.php')


def ticket(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    return render(request, 'CTF/lessons/IDOR/ticket.php', {'ticket': ticket})

def createticket(request):
    if request.method == 'POST':
        form = TicketsForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return redirect('ticket_view', ticket_id=ticket.id)
        else:
            error = 'ты чо творишь'
    else:
        form = TicketsForm()
    data = {'form': form}
    return render(request, 'CTF/lessons/IDOR/tickets.php', data)




class LoginUser( LoginView):
    form_class = LoginUserForm
    template_name = 'CTF/lessons/IDOR/login.php'
    success_url = 'IDOR/'

def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            login(request, user)
            return redirect('/CaptureTF/lessons/IDOR/')
    else:
        form = UserRegistrationForm()

    return render(request, 'CTF/lessons/IDOR/register.php', {'form': form})