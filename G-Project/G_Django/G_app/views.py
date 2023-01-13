from django.shortcuts import render
from django.http import HttpResponse

# electronics page
def electronics(request):
    return HttpResponse("<h2>Your are in electronics page</h2>")

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