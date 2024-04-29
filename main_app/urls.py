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
]
