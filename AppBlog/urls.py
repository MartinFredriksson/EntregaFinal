from django.urls import path
from AppBlog import views 

urlpatterns = [
    path("inicio" , views.inicio , name = "inicio"),
    path("padre", views.padre , name = "padre"),
    path("metas", views.metas , name = "metas"),



]
