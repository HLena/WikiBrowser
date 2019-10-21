from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from django.template import Template,Context
from .forms import Formulario
from consultas.models import WebPages, Words

import json


def index(request):
    #return HttpResponse("Vaya mi suerte")
    doc_html = open("/home/ghlene/django-apps/Buscador/templates/index.html")
    plt = Template(doc_html.read())
    doc_html.close()
    ctx = Context()
    document = plt.render(ctx)
    return HttpResponse(document)
    #  return render(request, 'index.html', context=context)

def index1(request):
    # #return HttpResponse("Vaya mi suerte")
    # doc_html = open("/home/ghlene/django-apps/Buscador/templates/index1.html")
    # plt = Template(doc_html.read())
    # doc_html.close()
    # ctx = Context()
    # document = plt.render(ctx)
    # return HttpResponse(document)
     return render(request, '../templates/index1.html')


def  resultados(request):
    keyword = request.GET.get('consulta')
    results = Words.objects.filter(word=keyword)
    results.query.join(WebPages)

    
    
    return render(request, '../templates/result.html',{'results':results})


