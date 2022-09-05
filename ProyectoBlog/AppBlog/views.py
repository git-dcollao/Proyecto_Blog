import datetime

from tempfile import template
from urllib import request

from django.contrib import messages
from django.shortcuts import render, redirect

from AppBlog.models import *
# Create your views here.

def inicio(request):

    return render(request, 'index.html', {})

def usuario(request):

    return render(request, 'index.html', {})

def tags(request):

    return render(request, 'index.html', {})

def categoria(request):

    return render(request, 'index.html', {})

def post(request):

    return render(request, 'index.html', {})

def comentarios(request):

    return render(request, 'index.html', {})
