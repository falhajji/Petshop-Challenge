from django import forms
from .models import Pets

class PetForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = '__all__'
