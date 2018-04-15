from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
	path('',views.home),
	path('login/',login,{'template_name':'accounts/login.html'}),
	path('profile/',views.home),
]
