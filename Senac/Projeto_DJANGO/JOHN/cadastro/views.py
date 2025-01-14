from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.

pessoas = Pessoa.objects.all()
contexto = {
    'title':'Cadastro - Salão de Beleza Visual da Moda',
    'pessoas': pessoas
}
def cadastro(request):
    return render(request,'cadastro/index.html', contexto)

def gravar(request):
    nova_pessoa = Pessoa()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.idade = request.POST.get('idade')
    nova_pessoa.email = request.POST.get('email')
    nova_pessoa.save()

    return cadastro(request)

def mostrar(request):    
    return render(request,'cadastro/mostrar.html', contexto)