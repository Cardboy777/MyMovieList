from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here
class MovieReview(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Django Secure User")
    movie_id = models.IntegerField(default=0)
    rating = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    review = models.CharField(max_length=1000, default='')
