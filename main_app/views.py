from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Add the following import
from django.http import HttpResponse

#Import Models from .models
from .models import Deck
from .models import Card


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def card_index(request):
   cards = Card.objects.all()
   return render(request, 'cards/index.html', {'cards': cards})

#Login Required Functionality

#Location Functionality
class DeckCreate(LoginRequiredMixin, CreateView):
    model = Deck
    fields = ['name', 'description', 'game']

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
   
class DeckUpdate(LoginRequiredMixin, UpdateView):
    model = Deck
    fields = ['name', 'description', 'game']

class DeckDelete(LoginRequiredMixin, DeleteView):
    model = Deck
    success_url = '/'
   