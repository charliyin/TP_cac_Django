from django import forms
from .models import Contacto

class ContactoForms(forms.ModelForm):
    class Meta:
        model = Contacto
        # fields = ["nombre", "correo", "asunto", "mensaje"]
        fields = '__all__'