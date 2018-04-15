from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	path('',views.home, name = 'home'),
	path('login/',login,{'template_name':'accounts/login.html'}),
	path('logout/',logout,{'template_name':'accounts/logout.html'}),
	path('register/',views.register, name='register'),
	path('profile/',views.profile, name='profile'),
]
