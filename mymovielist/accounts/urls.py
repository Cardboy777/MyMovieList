from django.urls import path
from . import views
from django.contrib.auth.views import login, logout
from django.conf.urls import include, url
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', login, {'template_name': 'accounts/login.html'}),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.change_password, name='change_password'),
    
]
