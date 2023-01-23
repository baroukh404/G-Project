from django.shortcuts import render
from django.shortcuts import loader
from django.shortcuts import redirect
from django.http import HttpResponse
# import requests
from .models import users
import os
import json
import re



url = 'http://localhost:8000/application/contact/?receiver=$recipient&sender=$originator&msg=$messagedata&id=$messageid'


def check_email(email):
	if re.search(r'@', email):
		pass
	else:
		headers = {
			"Content-Type" : "application/json"
		}
		body = {
			"email" : email
		}
		# headers, body = json.dumps(headers), json.dumps(body)
		# response = requests.post('/application/login/', headers=headers, data=body)
		# Send GET request to login page
		return redirect('/application/login/error=invalidemail')




def sendsms(request):
    if request.method == 'GET':
        receiver = request.GET.get('receiver')
        # receiver = request.GET.get('receiver')
        message = request.GET.get('msg')
        send = loader.get_template('contact.html')
        payload = {
            "receiver" : receiver,
            "message" : message
            }
        return HttpResponse(send.render(payload, request))
# def home(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse('home'))
#         else: 
#             messages.info(request,"Username or Password Invalid")
    
#     return render(request, 'login.html')
url = 'https://api.openai.com/v1/completions'
headers = {
	"Authorization" : "Bearer <API_KEY>",
	"Content-Type" : "application/json"
}
body = {
	"model" : "text-davinci-003",
	"prompt" : "Say me this is a test",
	"temperature" : 0,
	"stop" : "category"
}

body = json.dumps(body)
# def home(request):
# 	check_email(request.POST.get('username'))
# 	if request.method == 'POST':
# 		# get username
# 		username = request.POST.get('username')
# 		# get password
# 		password = request.POST.get('password')
# 		script = f"\
# 		Your name is : {username}<br>\
# 		Your password is : {password}"
# 		# data = f'{"name" : {username}, "password" : {password}}'
# 		data = {}
# 		data["name"] = username
# 		data["password"] = password
# 		# body  = json.dumps(data)
# 		return HttpResponse(body)
	

# 	elif request.method == 'GET':
# 		return HttpResponse("GET request")

		# return HttpResponse(f'<p>Your email is: {_type} and your password is : {_pwd_type}</p>')
		# return redirect('/application/login/')
	
	

		# _home_page = loader.get_template('home.html')
		# context = {
		# 	'user' : [username, password],
		# }
		# # return HttpResponse(_home_page.render(context, request))
		# return HttpResponse(f'<p>Your email is: {username} and your password is : {password}</p>')
	# else:
	# 	return redirect('/application/login/')

def contact(request):
	return HttpResponse('<h1>Contact Page</h1>')


def login(request):
	if request.method == 'GET':
		if request.GET.get('error'):
			return HttpResponse('Invalid Email')
		else:
			_login_page = loader.get_template('login.html')
			return HttpResponse(_login_page.render())


def home(request):
	# if request.method == 'POST':
		# username = request.POST.get('username')
	pg_home = loader.get_template('home.html')
	return HttpResponse(pg_home.render())

def bootstrap(request):
	pg_bootsrap = loader.get_template('bootstrap-v4.html')
	return HttpResponse(pg_bootsrap.render())
