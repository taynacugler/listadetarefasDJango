from django.shortcuts import render, redirect
from .models import Tarefas, checkedTarefas

# Create your views here.
def getTarefas(request):
    tarefas = Tarefas.objects.all()
    tarefas_concluidas = checkedTarefas.objects.all()
    return render(request, "index.html", {"tarefas": tarefas, "tarefas_concluidas": tarefas_concluidas})

def createTarefa(request):
    nome = request.POST.get("nome")
    if nome:
        if Tarefas.objects.filter(nome=nome).exists():
            mensagem_erro = "Nome já existe. Escolha um nome diferente."
        else:
            Tarefas.objects.create(nome=nome)
            mensagem_erro = None
    else:
        mensagem_erro = "Nome não pode ser vazio."

    tarefas = Tarefas.objects.all() 
    return render(request, "index.html", {"tarefas": tarefas, "mensagem_erro": mensagem_erro})

def updateTarefa (request, id):
    tarefas = Tarefas.objects.get(id=id)
    return render (request, "update.html", {"tarefas" : tarefas})

def update(request, id):
    novoNome = request.POST.get("nome")
    tarefas = Tarefas.objects.get(id=id)
    tarefas.nome = novoNome
    tarefas.save()
    return redirect (getTarefas)

def delete (request, id):
    tarefas = Tarefas.objects.get(id=id)
    tarefas.delete()
    return redirect (getTarefas)

def checkedTarefa (request, id):
        tarefa = Tarefas.objects.get(id=id)
        checkedTarefas.objects.create(nome=tarefa.nome)    
        tarefa.delete()
        return redirect (getTarefas)


