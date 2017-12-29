from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    """ Creation du formulaire pour s'enregistrer au site """

    prenom = forms.CharField(label='prenom', max_length=30, required=False)
    nom = forms.CharField(label='nom', max_length=30, required=False)
    email = forms.EmailField(label='email',max_length=100)

    class Meta:
        model = User
        fields = ('username', 'prenom', 'nom', 'email', 'password1', 'password2')
