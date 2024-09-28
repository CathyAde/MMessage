from django.contrib import admin
from django.urls import path
from inscription import views 


urlpatterns = [
   
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('', views.accueil, name='accueil'),
    #path('gestion_contact/', views.gestion_contact, name='gestion_contact'),
    #path('creer_contact/', views.creer_contact, name='creer_contact'), 
    
]
