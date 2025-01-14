from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.comentario, name='comentario'),  
    path('gravar_comentario/', views.gravar_comentario, name='gravar_comentario'), 
    # path('mostrar/', views.mostrar, name='mostrar'), 
    # path('editar/<int:id>', views.editar, name='editar'),
    path('<int:id>', views.apagar, name='apagar'),
    # path('atualizar/<int:id>', views.atualizar, name='atualizar'),
]