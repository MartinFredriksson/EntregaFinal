from django.shortcuts import render
from django.http import HttpResponse




def inicio(request):
     return render (request, "AppBlog/inicio.html")

def padre(request):
     return render (request,"AppBlog/padre.html" )
    

def metas(request):
     return render (request,"AppBlog/metas.html")


