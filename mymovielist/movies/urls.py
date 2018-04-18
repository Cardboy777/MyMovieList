from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.movies),
    path('search/', views.search, name='search_url'),
]
