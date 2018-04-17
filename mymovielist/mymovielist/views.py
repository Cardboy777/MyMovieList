from django.shortcuts import render, HttpResponse


# Create Views here
def about(request):
    return render(request, 'homepage/about.html')




def home(request):
    return render(request, 'homepage/home.html')
