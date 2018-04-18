from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MovieReview(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Django Secure User")
