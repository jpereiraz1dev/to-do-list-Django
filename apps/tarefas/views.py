from django.shortcuts import render,get_object_or_404,redirect
from .models import Tarefa
from .forms import TarefaForm
from django.contrib import messages
from datetime import datetime


# Create your views here.

def index(request):
        if not request.user.is_authenticated:
            messages.info(request,"Ops... Parece que voce ainda nao esta logado, que tal Criar uma conta e comecar a utilizar nosso app :) ")
            return redirect('cadastro')
        else:
            dados = Tarefa.objects.filter(user = request.user)
            dados = dados.order_by('situacao')
            return render(request,'tarefas/index.html',{'dados':dados,
                                                        'title': f'Minhas Tarefas como {request.user}'})


def explorer(request):
    try:
        dados = Tarefa.objects.exclude(user = request.user)
        dados = dados.exclude(publica = False)
        dados = dados.exclude(situacao = True)
        return render(request,'tarefas/index.html',{'dados':dados,
                                                    'title': 'Todas as Tarefas'})
    except:
        dados = Tarefa.objects.all()
        return render(request,'tarefas/index.html',{'dados':dados,
                                                    'title': 'Todas as Tarefas'})

def tarefa(request,tarefa_id):
    tarefa = get_object_or_404(Tarefa,pk=tarefa_id)
    
    return render(request,'tarefas/tarefa.html',{"tarefa":tarefa})

def nova_tarefa(request):
    if not request.user.is_authenticated:
        messages.info(request,"Voce precisa estar em uma conta para acessar a funcionalidade desejada. Se cadastre ou faca login abaixo")
        return redirect('cadastro')

    form = TarefaForm()
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False) #Nao salva ainda
            tarefa.user = request.user # Define o user
            if tarefa.situacao:
                tarefa.concluida_em = datetime.now()
            tarefa.save()
            form = TarefaForm()
            return redirect('index')


    context = {
                "form": form
            }

    return render(request,"tarefas/nova_tarefa.html",context)

def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id,user=request.user)

    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save(commit=False)
            if tarefa.situacao:
                tarefa.concluida_em = datetime.now()
            form.save()
            return redirect('index')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, "tarefas/editar_tarefa.html", {
        "form": form
    })

def deletar_tarefa(request,tarefa_id):
    tarefa = get_object_or_404(Tarefa,pk = tarefa_id,user=request.user)

    if request.method == 'POST':
        messages.success(request,f"Tarefa ({tarefa.nome}) excluida com sucesso")
        tarefa.delete()
        
    return redirect('index')
        
