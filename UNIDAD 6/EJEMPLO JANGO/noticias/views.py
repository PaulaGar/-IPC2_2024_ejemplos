from django.shortcuts import render #Ignorar
from django.http import HttpResponse
# Create your views here.

def saludo(request):
    return HttpResponse("<h2>Hola mundo</h2>")

def despedida(request):
    return HttpResponse("Adiós :D")