from django.shortcuts import render, HttpResponse

#Create Views here
def about(request):
    return render(request, 'home/about.html')
