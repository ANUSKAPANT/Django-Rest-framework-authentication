from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
# from rest_framework import generics, permissions
from .serializers import UserSerializer


from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'User':'/user-list/',
		'Register':'/user-register/',
		'Login':'/user-login/',
		}	

	return Response(api_urls)


@api_view(['GET'])
def userListView(request):
	user = User.objects.all()
	serializer = UserSerializer(user, many=True)
	return Response(serializer.data)



@api_view(['POST'])
def userRegisterView(request):

	if request.method == 'POST':
		serializer = UserSerializer(data=request.data)
		data = {}
		print (serializer)
		if serializer.is_valid():
			user = serializer.save()
			user.set_password(user.password)
			user.save()
			data['response'] = "successfully registered a new user"  
			data['email'] = user.email
			data['username'] = user.username
			token = Token.objects.get(user = user).key
			data['token'] = token
		else:
			data = serializer.errors
	return Response(data)


def homeView(request):
	return JsonResponse('Home page')



