from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sobre(request):
    return render(request, 'sobre/index.html')

def produtos(request):
    return render(request, 'sobre/produtos.html')

def servicos(request):
    return render(request, 'sobre/servicos.html')