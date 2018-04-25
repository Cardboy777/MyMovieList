from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import UserProfile
from django.core.files.images import get_image_dimensions


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
        field_order = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

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
        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
        )
        field_order = (
            'first_name',
            'last_name',
            'email',
            'password'
        )

class EditProfileForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':10,'cols':60}))
    class Meta:
        model=UserProfile
        fields = (
            'age',
            'city',
            'description'
        )
        field_order = (
            'age',
            'city',
            'description',
        )
    def clean_avatar(self):
        avatar=self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            max_width= max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                u'Please us an image that is '
                '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            pass
        return avatar
