from django.shortcuts import render, redirect
import tmdbsimple as tmdb
from movies.models import MovieReview

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
        movie_reviews =  MovieReview.objects.filter(movie_id=movie_id)
        args = {'title': movie_title, 'poster': movie_poster, 'overview': movie_overview, 'genres': movie_genres,
                'companies': movie_companies, 'release_date': movie_release_date, 'trailer': movie_trailer,
                'homepage': movie_homepage, 'director':movie_director, 'director_pic':movie_director_pic,'reviews':movie_reviews,}
    return render(request, 'movies/movies.html', args)


def search(request):
    search_query = request.GET.get('search_box')
    if search_query:
        search = tmdb.Search()
        x = 2
        result = search.movie(query = search_query, page = 1)
        num = search.total_pages
        print(num)
        #print(search.results)
        final = search.results
        while x <= 5:
            print(x)
            search.movie(query = search_query, page = x)
            #print(search.results)
            final.extend(search.results)
            x = x + 1
        args = {'results': final}
        return render(request, 'movies/search.html', args)
    else:
        return redirect('/')
