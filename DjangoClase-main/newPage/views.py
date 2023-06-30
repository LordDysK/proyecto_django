from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth import logout
from django.shortcuts import redirect

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
            username = form.cleaned_data['username']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            telefono = form.cleaned_data['telefono']
            fecha_nacimiento = form.cleaned_data['fechaNacimiento']


            usuario = Usuario.objects.create_user(
                correo=correo,
                password=password,
                username=username,
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                fechaNacimiento=fecha_nacimiento,

                
            )

            usuario.set_password(password)
            usuario.save()
            context = {"mensaje": "Registrado Correctamente"}
            return render(request, "pages/home.html", context)
    else:
        form = UsuarioForm()
    
    context = {"form": form, "mensaje": "No se ha podido registrar"}
    return render(request, "pages/creacion_user.html", context)


def nav(request):
    context = {}
    return render(request, "pages/navbar.html", context)

def tokens(request):
    context = {}
    return render(request, "pages/tokens.html", context)

def inicio_sesion(request):
    context = {}
    return render(request, "pages/inicio_sesion.html", context)


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']

            user = authenticate(correo=correo, password=password)
            if user:
                login(request, user)
                context={"mensaje": "registro"}
                return render(request,'pages/home.html',context)  # Corregido el nombre de la ruta
            else:
                context = {'login_error': 'Credenciales incorrectas, si no tienes cuenta regístrate.'}
                return render(request, 'pages/inicio_sesion.html', context)  # Corregido la ruta de la plantilla
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'pages/inicio_sesion.html', context)




def logout_view(request):
    logout(request)
    return redirect('loginview')


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


