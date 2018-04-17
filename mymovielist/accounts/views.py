from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from accounts.forms import RegistrationForm, EditProfileForm, EditUserForm
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
        else:
            return redirect('/account/register')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/register.html', args)


def view_profile(request):
    args = {'User': request.user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
<<<<<<< HEAD
	if request.method=='POST':
		UserForm = EditUserForm(request.POST, instance=request.user)
		ProfileForm = EditProfileForm(request.POST, instance=request.user.userprofile)
		if UserForm.is_valid() and ProfileForm.is_valid():
			UserForm.save()
			ProfileForm.save()
			return redirect('/account/profile')
		else:
			return redirect('/account/profile/edit')
	else:
		UserForm = EditUserForm(instance=request.user)
		ProfileForm = EditProfileForm(instance=request.user.userprofile)
		args = {'userform':UserForm,'profileform':ProfileForm}
		return render(request,'accounts/edit_profile.html',args)
=======
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
        else:
            return redirect('/account/profile/edit')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


>>>>>>> 94a88021ae16388ad939060baa75f0eddeb04a00
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/profile/password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
