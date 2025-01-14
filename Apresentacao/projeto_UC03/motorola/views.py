from django.shortcuts import render

# Create your views here.
def motorola(request):
    return render(request,
                  'motorola/index.html',
                 )