from django.shortcuts import render
from .models import Usuario
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
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            password = request.POST.get("password")
            Nom = form.cleaned_data['username']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            fechaNacimiento = form.cleaned_data['fecha']
            telefono = form.cleaned_data['telefono']

            print("tu mama es weona")
            usuario = Usuario.objects.create_user(
                correo=correo,
                password=password,
                Nom=Nom,
                nombre=nombre,
                apellido=apellido,
                fechaNacimiento=fechaNacimiento,
                telefono=telefono,
                activo=1,
            )
            print("y tu papa tambien")

            context = {"mensaje": "Registrado Correctamente"}
            return render(request, "pages/creacion_user.html", context)
    else:
        form = UsuarioForm()
    
    context = {"form": form, "mensaje": "No se ha podido registrar"}
    return render(request, "pages/creacion_user.html", context)


""" def userAdd(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            password = request.POST.get["password"]
            Nom = form.cleaned_data['username']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            fechaNacimiento = form.cleaned_data['fecha']
            telefono = form.cleaned_data['telefono']

            
            # Crea el usuario utilizando el administrador de usuarios
            usuario = Usuario.objects.create_user(
            correo=correo,
            Nom=Nom,
            nombre=nombre,
            apellido=apellido,
            fechaNacimiento=fechaNacimiento,
            telefono=telefono,
            activo=1,)

            usuario.set_password(password)
            usuario.save()
            

            
            context = {"mensaje": "Registrado Correctamente"}
            return render(request, "pages/creacion_user.html", context)
    else:
        form = UsuarioForm()
    
    context = {"form": form, "mensaje": "No se ha podido registrar"}
    return render(request, "pages/creacion_user.html", context)
 """
""" def userAdd(request):
    if request.method == "POST":
        Nom = request.POST["username"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        fecha = request.POST["fecha"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]
        password = request.POST.get["password"]
        creacion_user(correo,password)

        objUsuario = Usuario.objects.create(
            Nom=Nom,
            nombre=nombre,
            apellido=apellido,
            fechaNacimiento=fecha,
            correo=correo,
            telefono=telefono,
            activo=1,
        )
        objUsuario.save()
        context = {"mensaje": "Registrado Correctamente"}
        return render(request, "pages/creacion_user.html", context)
    else:
        context = {"mensaje": "No se a podido regristrar"}
        return render(request, "pages/creacion_user.html")
     """
def nav(request):
    context = {}
    return render(request, "pages/navbar.html", context)

def tokens(request):
    context = {}
    return render(request, "pages/tokens.html", context)

def inicio_sesion(request):
    context = {}
    return render(request, "pages/inicio_sesion.html", context)

""" def creacion_user(request):
    context = {}
    return render(request, "pages/creacion_user.html", context) """


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


