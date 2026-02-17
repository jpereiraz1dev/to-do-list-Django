from django.forms import ModelForm
from django import forms
from tarefas.models import Tarefa

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ["nome","descricao","publica","validade"]
        widgets = {
            'validade': forms.DateTimeInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            )
        }