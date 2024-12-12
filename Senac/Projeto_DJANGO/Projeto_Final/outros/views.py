from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def outros(request):
    return render(request, 'outros/index.html')

def atividade(request):
    return render(request, 'outros/atividade.html')