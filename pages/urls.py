from django.contrib import admin
from django.urls import path , include
from pages import views

urlpatterns = [
    path('', views.home , name='home'),
    path('login' , views.login , name='login'),
    path('explore' , views.explore, name = 'explore'),
    path('offers', views.offers , name='offers')
]
