from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


# Create your models here
class MovieReview(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    movie_id = models.IntegerField(default=0)
    movie_title = models.CharField(max_length=50, default='')
    rating = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    review = models.CharField(max_length=1000, default='')
