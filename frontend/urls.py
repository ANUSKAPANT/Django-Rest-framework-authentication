from django.urls import path
from . import views

urlpatterns = [
	path('', views.loginView, name='login'),
	path('register/', views.registerView, name='register'),	
	path('home/', views.homeView, name='home'),

]


