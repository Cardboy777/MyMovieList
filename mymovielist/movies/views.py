from django.shortcuts import render, HttpResponse

def movies(request) :
    return render(request, 'movies/movies.html')
