from django.shortcuts import render, HttpResponse

def ma_vue(request):
    return HttpResponse("Hellow world!")

def page2(request):
    return HttpResponse("Voici une autre page!")
