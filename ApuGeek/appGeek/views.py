# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template 
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from models import *
from django.shortcuts import get_object_or_404

from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required



def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.order_by("-comentarios").all()[:10]
    template = "index.html"
    #dicicionario = {"categorias":categorias,"enlaces" : enlaces}
    return render_to_response(template,locals())

def categoria(request, id_categoria):
    categorias = Categoria.objects.all()
    cat = get_object_or_404(Categoria,pk = id_categoria)
    #cat = Categoria.objects.get(pk = id_categoria)
    
    enlaces = Enlace.objects.filter(categoria = cat)
    template = "index.html"
    return render_to_response(template,locals())


