from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.TextField(null=True)
    original_title = models.TextField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.TextField(null=True)
    backdrop_path = models.TextField(null=True)
    release_date = models.TextField(null=True) # 개봉일자 일단.TextField로blank=True 받음
    popularity = models.FloatField(null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    adult = models.BooleanField(null=True)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_movies')
    # detail에서 가져올 필드
    # homepage = models.URLField(blank=True)
    # runtime = models.IntegerField(blank=True)
    # tagline = models.TextField(blank=True)

class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=20)
    movies = models.ManyToManyField(Movie, blank=True, related_name='genres')


class UserLikeGenre(models.Model):
    genre_id = models.IntegerField()
    profile = models.ManyToManyField(User, related_name='userLikeGenres')


# 월드컵 결과에 따른 추천 모델
class WorldcupRecommend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genre_rank1 = models.IntegerField()
    genre_rank2 = models.IntegerField()
