from django.contrib import admin
from django.urls import path, include
from inscription import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/', views.inscription, name='inscription'),
    path('activer/<uidb64>/<token>/', views.activate, name='activate'),
    path('confirmation-envoyee/', views.confirmation_sent, name='confirmation_sent'),
    path('connexion/', views.connexion, name='connexion'),
    path ('', views.accueil, name='accueil'),
    path ('gestion_contact/', views.gestion_contact, name='gestion_contact'),
    path ('creer_contact/', views.creer_contact, name='creer_contact'),
    path ('supprimer_contact/', views.supprimer_contact, name='supprimer_contact'),
    path ('modifier_contact/', views.modifier_contact, name='modifier_contact'),
    path ('importer_contact/', views.importer_contact, name='importer_contact'),
    path ('contacts_list/', views.contacts_list, name='contacts_list'),
    #path('importer_contact/importer-contact/', views.importer_contact, name='importer_contact'),
]


