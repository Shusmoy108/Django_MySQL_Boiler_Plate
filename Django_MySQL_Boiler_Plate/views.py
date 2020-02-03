from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world")

def templateexample(request):
    return render(request,'inheit_template.html', {'title': "Django_MySQL_Boiler_Plate","body":"inherit template page"})