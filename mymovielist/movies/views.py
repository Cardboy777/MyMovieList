from django.shortcuts import render, redirect

def movies(request) :
    return render(request, 'movies/movies.html')
def search(request) :
    search_query = request.GET.get('search_box')
    if search_query:
        args = {'search':search_query}
        return render(request,'movies/search.html',args)
    else:
        return redirect('/')
