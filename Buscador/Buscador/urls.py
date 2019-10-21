
# from django.conf.urls import patterns , include, url
from django.contrib import admin
from django.urls import path
from apps.views import index,index1,resultados
from apps.forms import busqueda
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index1, name='index'),
    path('resultados/', resultados, name='resultados'),

    #url(r'^', index1, name = 'search'),
    #url(r'^resultados/$' , busqueda, name ='busqueda'),

]
