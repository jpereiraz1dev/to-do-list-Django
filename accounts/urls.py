from django.contrib import admin
from django.urls import path
from accounts.views import user_login, cadastro

urlpatterns =[
    path('login/', user_login, name = "login"),
    path('cadastro/', cadastro, name = "cadastro")
]