from django.urls import path
from . import views
from .views import ContactListView

urlpatterns = [
    path('contacts/<int:id>/', views.contact_detail, name='contact_detail'),
    path('contacts/', views.contacts_list, name='contacts_list'),
    path('contacts/<int:id>/', views.contact_detail, name='contact_detail'),

    path('creer-contact/', views.creer_contact, name='creer_contact'),
    path('contacts_list/', views.contacts_list, name='contacts_list'), 
    path('creer_contact/', views.creer_contact, name='creer_contact'),
    path('supprimer_contact/', views.supprimer_contact, name='supprimer_contact'),
    path('modifier_contact/', views.modifier_contact, name='modifier_contact'),
    path('importer_contact/', views.importer_contact, name='importer_contact'),
    
]
