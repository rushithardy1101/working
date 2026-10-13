from django.shortcuts import render
from django.http import HttpResponse
def help(request):
    return HttpResponse("HI, This is web application")