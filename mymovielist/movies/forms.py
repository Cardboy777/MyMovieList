from django import forms
from django.contrib.auth.models import User
from movies.models import MovieReview

class write_review(forms.ModelForm):
    review = forms.CharField()
    rating = forms.IntegerField()

    class Meta:
        model=MovieReview
        fields=('rating','review')
        field_order=('rating','review')
