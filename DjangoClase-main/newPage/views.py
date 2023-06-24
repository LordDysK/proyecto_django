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

def userAdd(request):
    if request.method != "POST":
        tipo = tipoUsuario.objects.all()
        context = {"tipo": tipo}
        return render(request, "pages/creacion_user.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)
        objUsuario = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            appPaterno=appPaterno,
            appMaterno=appMaterno,
            fechaNacimiento=fecha,
            tipoUsuario=objTipo,
            correo=correo,
            telefono=telefono,
            activo=1,
        )
        objUsuario.save()
        context = {"mensaje": "OK Registrado Correctamente"}
        return render(request, "pages/creacion_user.html", context)
    
def nav(request):
    context = {}
    return render(request, "pages/navbar.html", context)

def tokens(request):
    context = {}
    return render(request, "pages/tokens.html", context)



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


