from django.urls import path
from AppLogin.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("register", register , name = "register"),
    path("login", login_request , name = "login"),
    path("logout", LogoutView.as_view(), name = "logout"),



]