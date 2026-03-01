from django.forms import ModelForm
from django import forms
from .models import Tarefa

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ["nome","descricao","publica","validade","situacao"]
        widgets = {
            'validade': forms.DateTimeInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            )
        }