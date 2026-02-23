from django.contrib import admin
from django.urls import path
from accounts.views import user_login, user_cadastro, user_logout

urlpatterns =[
    path('login/', user_login, name = "login"),
    path('cadastro/', user_cadastro, name = "cadastro"),
    path('logout/', user_logout, name = "logout")
]