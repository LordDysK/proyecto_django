from django.urls import path
from . import views

urlpatterns = [

    path("re4",views.re4,name="re4"),
    path("home",views.home,name="home"),
    path("contacto",views.contacto,name="contacto"),
    path("Gow",views.gow,name="Gow"),
    path("ktn",views.ktn,name="ktn"),
    path("hk",views.hk,name="hk"),
    path("Fh5",views.fh5,name="fh5"),
    path("seguridad",views.seguridad,name="seguridad"),
    path("catalogo",views.catalogo,name="catalogo"),
    path("creacion_user",views.userAdd,name="login")
  
]
