from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from django.template import Template,Context
from .models import WebPages, Words
import templates

import json


def index(request):
    #return HttpResponse("Vaya mi suerte")
    doc_html = open("/home/ghlene/django-apps/WikiBrowser/templates/index.html")
    plt = Template(doc_html.read())
    doc_html.close()
    ctx = Context()
    document = plt.render(ctx)
    return HttpResponse(document)
    #  return render(request, 'index.html', context=context)

def index1(request):
    return render(request,"index1.html")


def  resultados(request):
    keyword = request.GET.get('consulta')
    results = Words.objects.filter(word=keyword)
    results.query.join(WebPages)    
    return render(request, "result.html" ,{'results':results})


