from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	return render(request, 'accounts/home.html')
def register(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account/profile')
	else:
		form = UserCreationForm()

		args = {'form':form}
		return render(request, 'accounts/register.html',args)
def profile(request):
	args = {'User':request.user}
	return render(request,'accounts/profile.html',args)
