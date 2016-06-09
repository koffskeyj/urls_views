from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Welcome to the world's greatest webpage!")


def arsenal(request):
    return HttpResponse("Arsenal")


def tottenham(request):
    return HttpResponse("Tottenham, the worst")


def thierry(request):
    return HttpResponse("Thierry Henry")
