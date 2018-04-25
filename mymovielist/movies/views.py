from django.shortcuts import render, redirect, get_object_or_404
import tmdbsimple as tmdb
from movies.models import MovieReview
from movies.forms import write_review
import operator
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
            if (f["site"] == "YouTube" and f["type"] == "Trailer"):
                movie_trailer = "https://youtube.com/embed/" + f["key"]
                break;
        for f in movie.credits()["crew"]:
            if f["job"] == "Director" :
                movie_director = f["name"]
                movie_director_pic = f["profile_path"]
        movie_homepage = movie_info["homepage"]
        movie_reviews =  MovieReview.objects.filter(movie_id=movie_id)
        sum = 0;
        count = 0;
        for review in movie_reviews:
            sum += review.rating
            count += 1
        average = 'no reviews'
        if count > 0:
            average = sum / count

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
        ranking = 'No reviews'
        count = 1
        for x in sorted_rankings:
            print(movie_id)
            print(x[0])

            if x[0]==int(movie_id):
                print("here")
                ranking = count
                break
            count+=1

        args = {'ranking': ranking, 'average_rating': average, 'id' :movie_id, 'title': movie_title, 'poster': movie_poster, 'overview': movie_overview, 'genres': movie_genres,
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
            search.movie(query = search_query, page = x)
            #print(search.results)
            final.extend(search.results)
            x = x + 1
        args = {'results': final}
        return render(request, 'movies/search.html', args)
    else:
        return redirect('/')

def write_review_view(request):
    if not request.user.is_authenticated:
        return redirect('/account/login/')
    if request.method == 'POST':
        form = write_review(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            movie_id = request.POST.get('movie_id')
            movie = tmdb.Movies(movie_id)
            movie_info = movie.info()
            movie_title = movie_info["title"]
            review.user=request.user
            review.movie_id = movie_id
            review.movie_title = movie_title
            review.save()
            text = form.cleaned_data['review']
            return redirect('/account/profile/?p='+request.user.username)
        args = {'form':form, 'id': request.POST.get('movie_id')}
        return render(request,'movies/write_review.html',args)
    else:
        form = write_review()
        movie_id = request.GET.get('movie_id')
        args = {'form':form,'id':movie_id}
        return render(request, 'movies/write_review.html',args)
def edit_review_view(request):
    if not request.user.is_authenticated:
        return redirect('/account/login/')
    if request.method == "POST":
        review_id = request.POST.get('review_id')
        review = get_object_or_404(MovieReview,pk=review_id)
        form = write_review(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('/account/profile/?p='+request.user.username)
        else:
            args= {'form':form,'id':review_id}
            return render(request,'movies/edit_review.html',args)

    else:
        review_id = request.GET.get('review_key')
        review = get_object_or_404(MovieReview,pk=review_id)
        if review.user != request.user:
            return redirect('/')
        form = write_review(instance=review)
        args = {'form':form,'id': review_id}
        return render(request,'movies/edit_review.html',args)
