from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# electronics page
def facebook(request):
    template = loader.g
    return HttpResponse(template.render())

# mecanics page
def mecanics(request):
    return HttpResponse("<h2>Your are in mecanics page</h2>")

# mathematics page
def mathematics(request):
    return HttpResponse("<h2>Your are in mathematics page</h2>")

# machine page
def machine(request):
    return HttpResponse("<h2>Your are in machine page</h2>")

# english page
def english(request):
    return HttpResponse("<h2>Your are in english page</h2>")

# french page
def french(request):
    return HttpResponse("<h2>Your are in french page</h2>")