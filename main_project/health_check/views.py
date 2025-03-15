from django.shortcuts import render
from django.http import  HttpResponse
from django.template import loader

def index(request):
    return HttpResponse('Happy Testing :)')

def html_index(request):
    template = loader.get_template('health_check.html')
    return HttpResponse(template.render())