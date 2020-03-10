from django.urls import path #importujemy funkcje path Django
from . import views #importujemy wszystkie nasze widoki (views) z aplikacji blog
#Widok - nazwa funkcji która robi większość czynności z obsługą strony
from django.shortcuts import render

urlpatterns = [ #pierwszy wzorzec adresu URL
    path('', views.post_list, name='post_list'),
]
