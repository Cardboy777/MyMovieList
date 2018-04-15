from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from accounts.forms import RegistrationForm, EditProfileForm
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def home(request):
	return render(request, 'accounts/home.html')
def register(request):
	if request.method=='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account/login')
		else:
			return redirect('/account/register')
	else:
		form = RegistrationForm()

		args = {'form':form}
		return render(request, 'accounts/register.html',args)
def view_profile(request):
	args = {'User':request.user}
	return render(request,'accounts/profile.html',args)
def edit_profile(request):
	if request.method=='POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/account/profile')
		else:
			return redirect('/account/profile/edit')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form':form}
		return render(request,'accounts/edit_profile.html',args)
def change_password(request):
	if request.method=='POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/account/profile')
		else:
			return redirect('/account/profile/password')
	else:
		form=PasswordChangeForm(user=request.user)
		args = {'form':form}
		return render(request,'accounts/change_password.html',args)
