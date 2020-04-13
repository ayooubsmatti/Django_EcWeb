from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Products Page")


def new(request):
    return HttpResponse("New Page")

