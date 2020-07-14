from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def loginView(request):
	return render(request, 'template/login.html',{});

def registerView(request):
	return render(request, 'template/register.html',{});

def homeView(request):
	return render(request, 'template/home.html',{});

