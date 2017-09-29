from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

def Travel(request):
    return render(request, "Travel.html")

def EntryR(request):
    return HttpResponseRedirect('http://shaniu.site:8787')

def Main(request):
    return render(request, 'Main.html', )
    #return HttpResponse("Love you!")

def suzhou(request):
    return render(request, "suzhou.html")
