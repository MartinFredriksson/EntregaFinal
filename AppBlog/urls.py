from django.urls import path
from AppBlog import views 

urlpatterns = [
    path("inicio" , views.inicio , name = "inicio"),
    path("padre", views.padre , name = "padre"),
    path("metas", views.metas , name = "metas"),
    path("usuarios", views.leerusuarios , name = "usuarios"),
    path("eliminarUsuario<id>" , views.eliminarusuario , name = "eliminarUsuario"),
    path("editarUsuario/<usuario_nombre>/" , views.editarusuario , name = "editarUsuario"),
    path("usuarioFormulario" , views.usuarioFormulario , name = "usuarioFormulario"),
    path("leermas<id>",views.leermas , name= "leermas"),
    
]
