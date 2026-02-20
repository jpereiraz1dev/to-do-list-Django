from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    nome = models.CharField(max_length=20,blank=False,null=False)
    descricao = models.TextField(max_length=200,default="")
    publica = models.BooleanField(default=False)
    situacao = models.BooleanField(default=False)
    validade =  models.DateField(null=True,blank=True)
    concluida_em =  models.DateField(null=True,blank=True)


    def __str__(self):
        return f"{self.nome}"
    