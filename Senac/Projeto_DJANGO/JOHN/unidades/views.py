from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def unidades(request):
    return render(request,'unidades/index.html')