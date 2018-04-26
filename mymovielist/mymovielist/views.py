from django.shortcuts import render, HttpResponse
from movies.models import MovieReview
import tmdbsimple as tmdb
import operator
tmdb.API_KEY = 'dd1efeb24fd2185a41514dc64bb9ac02'
# Create Views here
def about(request):
    return render(request, 'homepage/about.html')




def home(request):
    all_reviews = MovieReview.objects.all()
    ratings = {}
    for review in all_reviews:
        id = review.movie_id
        reviews = MovieReview.objects.filter(movie_id=id)
        sum = 0
        count = 0
        for review in reviews:
            sum += review.rating
            count += 1
        average = sum / count
        ratings[id] = average

    sorted_rankings = sorted(ratings.items(), key=operator.itemgetter(1))

    sorted_rankings.reverse()
    top_5 = sorted_rankings[:5]
    top_movies = []
    count=1
    for review in top_5:
        review_id = review[0]
        movie = tmdb.Movies(review_id)
        movie_info = movie.info()
        movie_title = movie_info['title']
        movie_poster = 'http://image.tmdb.org/t/p/w185/' + movie_info["poster_path"]
        top_movies.append({'id':review_id,'title':movie_title,'poster':movie_poster,'rank':count})
        count+=1

    args = {'TopMovies':top_movies}
    return render(request, 'homepage/home.html',args)

def guccigang(request):
    return render(request, 'homepage/guccigang.html')
