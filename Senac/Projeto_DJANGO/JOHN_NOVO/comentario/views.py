from django.shortcuts import render
from .models import Comentarios

# Create your views here.

comentarios = Comentarios.objects.all()

contexto = {
    'title': 'Cadastro - Salão de Beleza Visual da Moda',
    'comentario': comentarios
}

def comentario(request):
    comentarios = Comentarios.objects.all()

    contexto = {
        'title': 'Cadastro - Salão de Beleza Visual da Moda',
        'comentarios': comentarios
    }

    return render(
                request,
                'comentario/index.html',
                contexto
                )




def gravar_comentario(request):
    # salvar os dados de contato
    novo_comentario = Comentarios()
    novo_comentario.id_comentario = request.POST.get('id_comentario')
    novo_comentario.nome = request.POST.get('nome')
    novo_comentario.descricao = request.POST.get('descricao')
    novo_comentario.save()

    comentarios = Comentarios.objects.all()

    contexto = {
        'title': 'Cadastro - Salão de Beleza Visual da Moda',
        'comentarios': comentarios
    }
    
    return render(
                request,
                'comentario/index.html',
                contexto
                )



def apagar(request, id):
    comentariox = Comentarios.objects.get(id_comentario=id)
    comentariox.delete()
    return comentario(request)

    # return comentario(request)



# FUNÇÃO MOSTRAR
# def mostrar(request):
#     comentarios = Comentarios.objects.all()

#     contexto = {
#         'title': 'Cadastro - Salão de Beleza Visual da Moda',
#         'comentarios': comentarios
#     }
    
#     return render(
#                 request,
#                 'comentario/index.html',
#                 contexto
#                 )