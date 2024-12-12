from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def local(request):
    return render(request, 'local/index.html')

def ondeestamos(request):
    return render(request, 'local/ondeestamos.html')