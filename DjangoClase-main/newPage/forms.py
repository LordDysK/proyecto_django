from .models import Usuario
from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class meta:
        model=Usuario
        fields = "_all_" 
