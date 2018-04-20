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
        movie_director = ""
        movie_director_pic = ""
        for f in movie.videos()["results"]:
            if f["site"] == "YouTube":
                movie_trailer = "https://youtube.com/embed/" + f["key"]
        for f in movie.credits()["crew"]:
            if f["job"] == "Director" :
                movie_director = f["name"]
                movie_director_pic = f["profile_path"]
        movie_homepage = movie_info["homepage"]
        args = {'title': movie_title, 'poster': movie_poster, 'overview': movie_overview, 'genres': movie_genres,
                'companies': movie_companies, 'release_date': movie_release_date, 'trailer': movie_trailer,
                'homepage': movie_homepage, 'director':movie_director, 'director_pic':movie_director_pic,}
    return render(request, 'movies/movies.html', args)


def search(request):
    search_query = request.GET.get('search_box')
    if search_query:
        search = tmdb.Search()
        response = search.movie(query = search_query)
        print(search.results)
        args = {'results': search.results}
        return render(request, 'movies/search.html', args)
    else:
        return redirect('/')
