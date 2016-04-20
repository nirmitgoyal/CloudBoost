from django.shortcuts import render
from django.http import HttpResponse


def cloudboost(request):
    return HttpResponse("Hello, world. This is home page")

def index(request, book_id):
    return HttpResponse("You're looking at question %s." % book_id)

def search(request, book_id):
    return HttpResponse("You're lking at question %s." % book_id)    

