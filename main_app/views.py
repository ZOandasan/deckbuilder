from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .forms import CardInDeckForm
from django.http import HttpResponse


# Add the following import
from django.http import HttpResponse

#Import Models from .models
from .models import Deck
from .models import Card
from .models import CardInDeck


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

def deck_index(request):
   decks = Deck.objects.all()
   return render(request, 'decks/index.html', {'decks': decks})

def deck_detail(request, deck_id):
   deck = Deck.objects.get(id=deck_id)
   cardsindeck_form = CardInDeckForm
   cards = Card.objects.filter(game=deck.game)
   cardsindeck = CardInDeck.objects.all()
   cards_not_in_deck = Card.objects.exclude(id__in = cardsindeck.all().values_list('id')) #Excludes all cards in any deck. I want all cards in THIS deck to be excluded.
   
   
   return render(request, 'decks/detail.html', {
      'deck': deck,
      'cards': cards,
      'cardsindeck': cardsindeck,
      'cardsindeck_form': cardsindeck_form,
   })

#Login Required Functionality

#Deck Functionality
class DeckCreate(LoginRequiredMixin, CreateView):
    model = Deck
    fields = ['name', 'description', 'game']
    success_url = '/decks/'

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
   
class DeckUpdate(LoginRequiredMixin, UpdateView):
    model = Deck
    fields = ['name', 'description', 'game']
    success_url = '/decks/'

class DeckDelete(LoginRequiredMixin, DeleteView):
    model = Deck
    success_url = '/decks/'

#CardsInDeck Functionality

@login_required
def add_cardindeck(request, deck_id, card_id):
    deck = Deck.objects.filter(id=deck_id).first()
    card = Card.objects.get(id=card_id)
    if deck:
        return redirect('detail', deck_id=deck_id)

    form = CardInDeckForm(request.POST)
    if form.is_valid():
        new_cardindeck = form.save(commit=False)
        new_cardindeck.deck = deck
        new_cardindeck.card = card
        new_cardindeck.save()
    return redirect('detail', deck_id=deck_id)


class CardsInDeckUpdate(LoginRequiredMixin, UpdateView):
    model = CardInDeck
    fields = ['quantity']
    success_url = '/decks/'

    def form_valid(self, form):
        edit_cardsindeck = form.save(commit=False)
        print(edit_cardsindeck.user)
        if self.request.user.id != edit_cardsindeck.user.id:
            return redirect('detail', deck_id=edit_cardsindeck.deck.id)
        return super().form_valid(form)
    
    def get_success_url(self):
        obj = self.get_object()
        return redirect('index')


class CardsInDeckDelete(LoginRequiredMixin, DeleteView):
    model = CardInDeck
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        if self.object.user.id == request.user.id:
            self.object.delete()
        return redirect('detail', deck_id=self.object.deck.id)

    def get_success_url(self):
        obj = self.get_object()
        print(obj)
        return reverse('detail', kwargs={'deck_id': obj.deck.id})
    
#GENERATE TEXT FILE
def deck_text(request, deck_id):
    cards = CardInDeck.objects.all()
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=deck.txt'

    lines = []
    for card in cards:
        if card.deck.id == deck_id:
          lines.append(f'{card.quantity} {card.card.name}\n')

    response.writelines(lines)
    return response
