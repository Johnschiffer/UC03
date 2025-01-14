from django.shortcuts import render

# Create your views here.
def localizacao(request):
    return render(request,
                  'localizacao/index.html',
                 )