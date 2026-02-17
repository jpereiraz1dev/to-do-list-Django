from django.shortcuts import render,get_object_or_404,redirect
from tarefas.models import Tarefa
from tarefas.forms import TarefaForm

# Create your views here.

def index(request):
    dados = Tarefa.objects.filter(publica=True)

    return render(request,'index.html',{'dados':dados})

def tarefa(request,tarefa_id):
    tarefa = get_object_or_404(Tarefa,pk=tarefa_id)
    
    return render(request,'tarefa.html',{"tarefa":tarefa})

def nova_tarefa(request):
    form = TarefaForm()
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save()
            form = TarefaForm()
            return redirect('index')


    context = {
                "form": form
            }

    return render(request,"nova_tarefa.html",context)