from django.shortcuts import render
from .models import Pessoa

# Create your views here.
pessoas = Pessoa.objects.all()

contexto = {
    'title': 'Cadastro - Salão de Beleza Visual da Moda',
    'pessoas': pessoas
}
def cadastro(request):
    return render(
                request,
                'cadastro/index.html',
                contexto
                )

def gravar(request):
    # salvar os dados de contato
    nova_pessoa = Pessoa()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.idade = request.POST.get('idade')
    nova_pessoa.email = request.POST.get('email')
    nova_pessoa.save()

    return cadastro(request)

def mostrar(request):
    pessoas = Pessoa.objects.all()

    contexto = {
        'title': 'Cadastro - Salão de Beleza Visual da Moda',
        'pessoas': pessoas
    }
    
    return render(
                request,
                'cadastro/mostrar.html',
                contexto
                )

# FUNÇÃO EDITAR, ATUALIZAR, APAGAR
def editar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    return render(request,'cadastro/editar.html', {'pessoa': pessoa})


def atualizar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.nome = request.POST.get('nome')
    pessoa.idade = request.POST.get('idade')
    pessoa.email = request.POST.get('email')
    pessoa.save()

    return mostrar(request)

def apagar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.delete()
    return mostrar(request)