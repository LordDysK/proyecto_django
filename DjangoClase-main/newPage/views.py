from django.shortcuts import render
from .models import Usuario, tipoUsuario
from .forms import UsuarioForm

# Create your views here.



def catalogo(request):
    context = {}
    return render(request, "pages/catalogo.html", context)

def re4(request):
    context = {}
    return render(request, "pages/Re4.html", context)

def home(request):
    context = {}
    return render(request, "pages/home.html", context)

def contacto(request):
    context = {}
    return render(request, "pages/contacto.html", context)

def seguridad(request):
    context = {}
    return render(request, "pages/seguridad.html", context)

def gow(request):
    context = {}
    return render(request, "pages/GOW.html", context)

def ktn(request):
    context = {}
    return render(request, "pages/KTN.html", context)

def fh5(request):
    context = {}
    return render(request, "pages/FH5.html", context)

def tokens(request):
    context = {}
    return render(request, "pages/tokens.html", context)

def hk(request):
    context = {}
    return render(request, "pages/hk.html", context)
""" 
def ktn(request):
    context = {}
    return render(request, "pages/KTN.html", context)
def ktn(request):
    context = {}
    return render(request, "pages/KTN.html", context)
def ktn(request):
    context = {}
    return render(request, "pages/KTN.html", context)
 """


