from django.shortcuts import render, redirect
import tmdbsimple as tmdb
tmdb.API_KEY = 'dd1efeb24fd2185a41514dc64bb9ac02'
def movies(request) :
    movie_id = request.GET.get('movie_id')
    movie = tmdb.Movies(movie_id)
    movie_info = movie.info()
    return render(request, 'movies/movies.html')
def search(request) :
    search_query = request.GET.get('search_box')
    if search_query:
        args = {'search':search_query}
        return render(request,'movies/search.html',args)
    else:
        return redirect('/')
