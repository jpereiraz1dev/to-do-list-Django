from django.contrib import admin
from django.urls import path
from .views import index,tarefa,nova_tarefa,explorer, editar_tarefa,deletar_tarefa

urlpatterns =[
    path('',index, name='index'),
    path('explorer',explorer, name='explorer'),
    path('tarefa/<int:tarefa_id>/',tarefa,name="tarefa"),
    path('nova_tarefa/', nova_tarefa ,name="nova_tarefa"),
    path('deletar_tarefa/<int:tarefa_id>', deletar_tarefa ,name="deletar_tarefa"),
    path('editar_tarefa/<int:tarefa_id>', editar_tarefa ,name="editar_tarefa"),
]