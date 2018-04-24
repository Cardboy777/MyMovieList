from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.movies),
    path('search/', views.search, name='search_url'),
    path('write_review/',views.write_review_view, name='write_review'),
    path('edit_review/',views.edit_review_view, name='edit_review'),
]
