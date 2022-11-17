from django.urls import path
from . import views

urlpatterns = [
    path('worldcup/', views.worldcup, name='worldcup'),
    path('worldcup/recommend/', views.worldcup_recommend, name='worldcup_recommend'),
]