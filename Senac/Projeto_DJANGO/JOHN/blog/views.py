from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    #print('Passei pelo Blog')
    
    #return HttpResponse('<body bgcolor="green"><h1>Hellow World</h1></body>')

    return render(request, 'blog/index.html')


def artigo(request):
    return render(request, 'blog/artigo.html')

def doc(request):
    print("Passei no doc")
    return render(request, 'blog/doc.html')