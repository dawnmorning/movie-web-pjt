from django.urls import path
from . import views

urlpatterns = [

    # path('review/', views.reviews, name='reviews'),
    path('review/create/', views.review_c, name='review_c'),


]