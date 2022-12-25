from django.urls import path
from . import views


# 'api/v3/'
urlpatterns = [

    path('reviews/', views.reviews, name='reviews'),
    path('reviews/<str:username>/', views.my_reviews, name='my_reviews'),
    path('review/<int:review_pk>/detail/', views.review_r, name='review_r'),
    path('review/create/<int:movie_pk>/', views.review_c, name='review_c'),
    path('review/update/<int:review_pk>/', views.review_u, name='review_u'),
    path('review/delete/<int:review_pk>/', views.review_d, name='review_d'),
    path('review/like/<int:review_pk>/', views.review_like, name='review_like'),
    
    path('comment/<int:comment_pk>/', views.comment_ru, name='comment_ru'),
    path('comment/create/<int:review_pk>/', views.comment_c, name='comment_c'),
    path('comment/delete/<int:comment_pk>/', views.comment_d, name='comment_d'),
    path('comment/like/<int:comment_pk>/', views.comment_like, name='comment_pk'),

]