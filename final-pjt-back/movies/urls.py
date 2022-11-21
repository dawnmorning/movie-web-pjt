from django.urls import path
from . import views

urlpatterns = [

    path('worldcup/', views.worldcup, name='worldcup'),
    path('worldcup/recommend/', views.worldcup_recommend, name='worldcup_recommend'),
    path('movies/', views.movies_r, name='movies_r'),
    path('<int:movie_pk>/movies/', views.movie_r, name='movie_r'),
    path('movies/random/', views.randomMovies_r, name='randomMovies_r'),
    path('movies/like/<int:movie_pk>/', views.movie_like, name='movie_like'),

]