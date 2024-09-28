from urllib import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str  # Correction ici
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.tokens import default_token_generator as token_generator

  
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Utilisation correcte du formulaire
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Désactiver l'utilisateur jusqu'à la confirmation
            user.save()

            # Envoi de l'email de confirmation
            current_site = get_current_site(request)
            mail_subject = 'Activez votre compte'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': uid,
                'token': token,
            })
            send_mail(
                mail_subject,
                strip_tags(message),  # Email sans HTML pour le backup
                'noreply@tonsite.com',
                [user.email],
                html_message=message
            )

            return redirect('confirmation_sent')  # Redirige vers une page informant l'utilisateur de vérifier ses emails
    else:
        form = CustomUserCreationForm()  # Remplace par le formulaire vide pour GET

    return render(request, 'inscription.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))  # Utiliser force_str pour éviter les erreurs de version Django
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')  # Redirige l'utilisateur vers la page de connexion après activation
    else:
        return render(request, 'activation_invalid.html')  # Page d'erreur en cas d'activation échouée 
    
def confirmation_sent(request):
    return render(request, 'confirmation_sent.html')       


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user) 
            return redirect('accueil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')      
    return render(request, 'connexion.html')


def gestion_contact(request):
    return render(request, 'gestion_contact.html') 


def creer_contact(request):
    return render(request, 'creer_contact.html') 


def supprimer_contact(request):
    return render(request, 'supprimer_contact.html') 


def modifier_contact(request):
    return render(request, 'modifier_contact.html')


def importer_contact(request):
    return render(request, 'importer_contact.html')  


def contacts_list(request):
    return render(request, 'contacts_list.html')


@login_required
def accueil(request):
    return render(request, 'accueil.html')
