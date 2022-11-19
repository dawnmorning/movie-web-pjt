from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

User = settings.AUTH_USER_MODEL
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

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(User, related_name='like_reviews')


class Comment(models.Model):
    content = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(User, related_name='like_comments')

