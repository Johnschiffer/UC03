from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),  
    path('gravar/', views.gravar, name='gravar'),
    path('mostrar/', views.mostrar, name='mostrar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('apagar/<int:id>', views.apagar, name='apagar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
]