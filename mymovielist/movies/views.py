from django.shortcuts import render, redirect
import tmdbsimple as tmdb

tmdb.API_KEY = 'dd1efeb24fd2185a41514dc64bb9ac02'


def movies(request):
    movie_id = request.GET.get('movie_id')
    movie = tmdb.Movies(movie_id)
    if(movie_id):
        movie_info = movie.info()
        movie_title = movie_info["title"]
        movie_poster = 'http://image.tmdb.org/t/p/w185/' + movie_info["poster_path"]
        movie_overview = movie_info["overview"]
        movie_genres = movie_info["genres"]
        movie_companies = movie_info["production_companies"]
        movie_release_date = movie_info["release_date"]
        movie_trailer = ""
        for f in movie.videos()["results"]:
            if f["site"] == "YouTube":
                movie_trailer = "https://youtube.com/embed/" + f["key"]

        movie_homepage = movie_info["homepage"]
        args = {'title': movie_title, 'poster': movie_poster, 'overview': movie_overview, 'genres': movie_genres,
                'companies': movie_companies, 'release_date': movie_release_date, 'trailer': movie_trailer,
                'homepage': movie_homepage}
    return render(request, 'movies/movies.html', args)


def search(request):
    search_query = request.GET.get('search_box')
    if search_query:
        search = tmdb.Search()
        response = search.movie(query = search_query)
        args = {'search': response}
        return render(request, 'movies/search.html', args)
    else:
        return redirect('/')
