
from django.contrib import admin
from django.urls import path
from consultas.views import index,index1,resultados
from django.conf.urls import url, include


urlpatterns = [
    url('', index1, name='index'),
    url('resultados/', resultados, name='resultados'),
]