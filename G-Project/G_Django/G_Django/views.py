from django.shortcuts import render
from django.http import HttpResponse

# Home page
def home(request):
    return HttpResponse("<h1>Bonjour Rova Herve</h1>")

# Contact Page
def contact(request):
    return HttpResponse("<h1>Your are in contact page</h1>")

# Admin Page
def user(request):
    return HttpResponse("<h1>Your are in user page</h1>")

# Registration Page

def register(request):
    return HttpResponse("<h1>Your are in register page</h1>")