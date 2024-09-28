from django.db import models
from django.core.exceptions import ValidationError
import re


def validate_phone_number(value):
    # Congo: +242, Cameroun: +237
    pattern = r'^(\+242|00242|\+237|00237)\d{7,8}$'
    if not re.match(pattern, value):
        raise ValidationError("Le numéro de téléphone doit être au format congolais ou camerounais avec 9 à 10 chiffres.")


class Contact(models.Model):
    prenom = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, validators=[validate_phone_number])

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    
    
