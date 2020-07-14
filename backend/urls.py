from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('api-auth-token/', obtain_auth_token, name="login"),
	path('user-list/', views.userListView, name="user-list"),
	path('user-register/', views.userRegisterView, name="user-register"),
]