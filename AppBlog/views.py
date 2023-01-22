from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import Usuario , imagenes
from AppBlog.forms import *
from django import db
from django.contrib.auth.decorators import login_required
db.connections.close_all()





def inicio(request):
     return render (request, "AppBlog/inicio.html")

def padre(request):
     return render (request,"AppBlog/padre.html" )
    
def metas(request):
     return render (request,"AppBlog/metas.html")

def usuarios(request):
     return render (request, "AppBlog/usuarios.html")

def leerusuarios(request):
     usuarios = Usuario.objects.all()
     contexto = {"usuarios" : usuarios}
     return render(request, "AppBlog/usuarios.html" , contexto)
@login_required
def eliminarusuario (request, id):
     usuarios = Usuario.objects.get(id=id)
     print(usuarios)
     usuarios.delete()
     usuarios = Usuario.objects.all()
     return render(request, "AppBlog/usuarios.html" , {"usuarios" : usuarios})
@login_required   
def usuarioFormulario(request):
     if request.method=="POST":
          form= usuarioForm(request.POST)

          if form.is_valid():
               informacion=form.cleaned_data
               nombre= informacion["nombre"]
               apellido= informacion["apellido"]
               
               usuarios = Usuario(nombre=nombre, apellido=apellido)
               usuarios.save()
               usuarios = Usuario.objects.all()

               return render(request, "AppBlog/usuarios.html" , {"usuarios" : usuarios})
          else:
               return render(request, "AppCoder/crearusuario.html" )

     else:
          formulario = usuarioForm()
          return render (request, "AppBlog/crearusuario.html" , {"form" : formulario})
@login_required
def editarusuario(request, id):
    usuario=Usuario.objects.get(id=id)
    if request.method=="POST":
        formulario = usuario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.nombre=informacion["nombre"]
            usuario.apellido=informacion["apellido"]
            
            usuario.save()
            usuario=Usuario.objects.all()
            return render(request, "AppBlog/usuarios.html" ,{"usuario":usuario})
            pass
    else:
     formulario = usuarioForm (initial={"nombre":usuario.nombre, "apellido":usuario.apellido})
     return render(request, "AppBlog/editarusuario.html", {"form": formulario, "usuario": usuario}) 


def leermas(request, id):
     usuario=Usuario.objects.get(id=id)
     if request.method=="POST":
          formulario = usuario(request.POST)
          usuario.save()
          usuario=Usuario.objects.all()
          lista = imagenes.objects.filter(user= request.user)
          if len(lista)!=0:
               imagenes = lista[0].imagen.url
          else:
               imagenes = ""
   
          return render(request, "AppBlog/leermas.html" ,{"usuario":usuario , "imagenes": imagenes})
     else:
          return render(request, "AppBlog/leermas.html" ,{"usuario":usuario})


def leermas(request, id):
     usuario=Usuario.objects.get(id=id)
     if usuario != leermas:
          return render(request, "AppBlog/leermas.html" ,{"usuario":usuario , "imagenes": imagenes})
     else:
          return render(request, "AppBlog/leermascarla.html" ,{"usuario":usuario , "imagenes": imagenes})


     


