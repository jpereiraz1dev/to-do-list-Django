from django.shortcuts import render,get_object_or_404,redirect
from tarefas.models import Tarefa
from tarefas.forms import TarefaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    dados = Tarefa.objects.filter(user = request.user)

    return render(request,'tarefas/index.html',{'dados':dados})

def explorer(request):
    no_user = request.user
    dados = Tarefa.objects.exclude(user = request.user)

    return render(request,'tarefas/index.html',{'dados':dados})

def tarefa(request,tarefa_id):
    tarefa = get_object_or_404(Tarefa,pk=tarefa_id)
    
    return render(request,'tarefas/tarefa.html',{"tarefa":tarefa})

def nova_tarefa(request):
    if not request.user.is_authenticated:
        messages.info(request,"Voce precisa estar logado para acessar a funcionalidade desejada. Faca o login abaixo")
        return redirect('login')

    form = TarefaForm()
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False) #Nao salva ainda
            tarefa.user = request.user # Define o user
            tarefa.save()
            form = TarefaForm()
            return redirect('index')


    context = {
                "form": form
            }

    return render(request,"tarefas/nova_tarefa.html",context)