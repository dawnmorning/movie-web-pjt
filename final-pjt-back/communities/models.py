from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie
from accounts.models import Profile
# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(
        validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
        ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, related_name='author_profile')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')


class Comment(models.Model):
    content = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')

