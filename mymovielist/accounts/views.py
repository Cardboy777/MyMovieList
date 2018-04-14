from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	number = {1,2,3,4,5}
	name ='Daniel'
	args = {'myname':name,'numbers':number}
	return render(request, 'accounts/home.html', args)
