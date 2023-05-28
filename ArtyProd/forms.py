from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
class UserRegistrationForm(UserCreationForm):
  first_name = forms.CharField(label='Prénom')
  last_name = forms.CharField(label='Nom')
  email = forms.EmailField(label='Adresse e-mail')
 
  class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')

class ContactForm(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField()
    content = forms.CharField()







