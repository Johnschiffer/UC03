from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contato(request):
    print('Passei pelo Blog')
    
    return HttpResponse('<body bgcolor="grey"><h1>Contato</h1><P>JOHN</body>')
