from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import RegisterForm
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            # Verifica se existe um destino "next" na URL, senão vai para o index
            next_url = request.GET.get('next', 'index')
            return redirect(next_url)
        else:
            messages.error("Usuario ou Senha invalidos. ")
    else:
        form = AuthenticationForm()
     
    return render(request,'accounts/login.html',{"form" : form})

def cadastro(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request,'accounts/cadastro.html',{"form" : form})
