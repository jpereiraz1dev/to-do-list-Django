from django.contrib import admin
from django.urls import path
from tarefas.views import index,tarefa,nova_tarefa

urlpatterns =[
    path('',index, name='index'),
    path('tarefa/<int:tarefa_id>/',tarefa,name="tarefa"),
    path('nova_tarefa/', nova_tarefa ,name="nova_tarefa")
]