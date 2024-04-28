from django.contrib import admin

# Register your models here.
from .models import Card
from .models import Deck

# Register your models here
admin.site.register(Card)
admin.site.register(Deck)