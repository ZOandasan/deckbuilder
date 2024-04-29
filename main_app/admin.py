from django.contrib import admin

# Register your models here.
from .models import Card
from .models import Deck
from .models import CardInDeck

# Register your models here
admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(CardInDeck)