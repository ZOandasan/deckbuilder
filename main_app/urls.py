from django.urls import path, include
from . import views

urlpatterns = [
    #NAV PATHS
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.card_index, name='index'),
    #USER PATHS
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    #CARD PATHS
    path('cards/', views.card_index, name='index'),
]
