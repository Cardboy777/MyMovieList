from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
class EditUserForm(UserChangeForm):
    def __init__(self, *args, **kw):
        super(UserChangeForm, self).__init__(*args,**kw)
        self.fields.keyOrder = [
            'first_name',
            'last_name',
            'email',
            'password'
        ]
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'email',
            'password'
        }
class EditProfileForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        fields = {
            'age',
            'city',
            'description'
        }
