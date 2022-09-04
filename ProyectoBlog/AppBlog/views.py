import datetime

from tempfile import template
from urllib import request

from django.contrib import messages
from django.shortcuts import render, redirect

from AppBlog.models import *
# Create your views here.

def inicio(request):

    return render(request, 'index.html', {})


#
#ef BlogCRUD(request):
#
#   return render(request, 'index.html', {})
#
#
#
#ef BlogBuscar(request):
#
#   return render(request, 'index.html', {})