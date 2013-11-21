# coding: utf-8

from django.shortcuts import render, get_object_or_404

from .models import Noticia


def detalhe(request, id):
    noticia = get_object_or_404(Noticia, pk=id)
    return render(request, 'noticias/detalhe.html', {'noticia': noticia})
