from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog),
    path('doc/', views.doc),
    path('artigo/', views.artigo),
]