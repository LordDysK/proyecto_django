from .models import Usuario
from django.forms import ModelForm
from django import forms

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario  # Especifica la clase de modelo Usuario
        fields = '__all__'  # O especifica los campos que deseas incluir en el formulario