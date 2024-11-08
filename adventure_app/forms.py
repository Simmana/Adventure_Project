from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Place

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'created_at']