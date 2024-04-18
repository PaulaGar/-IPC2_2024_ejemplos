from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludo(response):
    return HttpResponse('<h1>HOLA MUNDO</h1>')

def bienvenida(response):
    return HttpResponse('<h2> Bienvenidos al laboratorio </h2>')