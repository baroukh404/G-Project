from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import user

# electronics page
def users(request):

    # Get the data in the models
    data = user.objects.all()

    # Get template page
    template = loader.get_template('users.html')

    # make the data in json file
    context = {
        'user' : data,
    }

    # Return an HttpResponse
    return HttpResponse(template.render(context, request))





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