from pyexpat.errors import messages
import re
from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
import csv
import io
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from MMessage.GestionContact.forms import ContactForm
from .models import Contact
# Create your views here.


def contact_detail(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, 'contact_detail.html', {'contact': contact})

def gestion_contact(request):
    contacts = Contact.objects.all()
    return render(request, 'gestion_contact.html', {'contacts': contacts})

def creer_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre le contact dans la base de données
            return redirect('some_view')  # Remplace 'some_view' par la vue vers laquelle rediriger après l'enregistrement
    else:
        form = ContactForm()    
    return render(request, 'creer_contact.html')


def validate_phone_number(phone):
    pattern = r'^(\+242|00242|\+237|00237)\d{7,8}$'
    return re.match(pattern, phone) is not None


def creer_contact(request):
    if request.method == 'POST':
        # Utiliser le formulaire ContactForm pour valider et sauvegarder le contact
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupérer les données et valider le numéro de téléphone
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            if not validate_phone_number(phone):
                return render(request, 'creer_contact.html', {'form': form, 'error': "Le numéro de téléphone doit être congolais ou camerounais avec 9 à 10 chiffres."})
            # Sauvegarder le contact
            form.save()
            print(f"Contact créé : {name} - {phone}")  # Vérification de la création
            return redirect('contacts_list')  # Rediriger vers la liste des contacts
    else:
        form = ContactForm()  # Créer une nouvelle instance du formulaire

    return render(request, 'creer_contact.html', {'form': form})


def importer_contact(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        # Lire le fichier CSV
        reader = csv.reader(file.read().decode('utf-8').splitlines())
        for row in reader:
            nom, telephone, email = row
            contact = Contact(nom=nom, telephone=telephone, email=email)
            contact.save()
        # Rediriger vers la liste des contacts après importation
        return redirect('contacts_list')
    return render(request, 'importer_contact.html')


def modifier_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        contact.nom = request.POST.get('nom')
        contact.telephone = request.POST.get('telephone')
        contact.email = request.POST.get('email')
        contact.save()
        return redirect('contacts_list')  # Redirige vers la liste des contacts
    return render(request, 'modifier_contact.html', {'contact': contact})


def supprimer_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('contacts_list')  # Redirige vers la liste des contacts


def contacts_list(request):
    contacts = Contact.objects.all()  # Récupérer tous les contacts
    return render(request, 'contacts_list.html', {'contacts_list': contacts})  # Remplacez par le nom de votre template
