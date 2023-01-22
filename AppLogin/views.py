from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from AppLogin.forms import RegistroUsuarioForm
from django.contrib.auth import login, authenticate



def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "AppLogin/registroexitoso.html")
        else:
            return render(request, "AppLogin/register.html", {"form": form, "mensaje": "ERROR AL CREAR EL USUARIO!"})
    else: 
        form = RegistroUsuarioForm()
        return render(request, "AppLogin/register.html" , {"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usu = info ["username"]
            clave = info ["password"]
            usuario = authenticate(username = usu , password = clave)
            if usuario is not None:
                login(request,usuario)
                return render(request, "AppLogin/registroexitoso.html")
            else:
                return render(request, "AppLogin/login.html")
        else:
            return render(request, "AppLogin/login.html")
    else: 
        form = AuthenticationForm()
        return render (request, "AppLogin/login.html", {"form" : form})
