from django.forms import ModelForm
from .models import CardInDeck

class CardInDeckForm(ModelForm):
  class Meta:
    model = CardInDeck
    fields = []