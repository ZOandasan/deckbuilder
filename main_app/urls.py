from django.urls import path, include
from . import views

urlpatterns = [
    #NAV PATHS
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #USER PATHS
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    #CARD PATHS
    path('cards/', views.card_index, name='index'),
    #DECK PATHS
    path('decks/', views.deck_index, name='index'),
    path('decks/decks/<int:deck_id>/', views.deck_detail, name='detail'),
    path('decks/create/', views.DeckCreate.as_view(), name='decks_create'),
    path('decks/<int:pk>/update/', views.DeckUpdate.as_view(), name='decks_update'),
    path('decks/<int:pk>/delete/', views.DeckDelete.as_view(), name='decks_delete'),
    #CARDINDECK PATHS
    path('decks/<int:deck_id>/cardsindeck/<int:card_id>/', views.add_cardindeck, name='cardsindeck_create'),
    #path('decks/<int:pk>/update_cardsindeck/', views.CardsInDeckUpdate.as_view(), name='cardindeck_update'),
    #path('decks/<int:pk>/delete_cardsindeck/', views.CardsInDeckDelete.as_view(), name='cardindeck_delete'),

    #DECK TO TEXT PATH
    path('decks/<int:deck_id>/decktotext/', views.deck_text, name='deck_text'),
]
