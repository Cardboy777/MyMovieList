from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Django Secure User")
    description = models.CharField(max_length=1000, default='Enter Something about your Movie Tastes and Background')
    city = models.CharField(max_length=30, default='ZA WARUDO')
    age = models.IntegerField(default=0
	    ,validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])

    # reviews = models.ManyToManyField(MovieReview, verbose_name="List of Reviewed Movies")

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
