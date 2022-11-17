from django.urls import path
from . import views

urlpatterns = [
    path('worldcup/', views.Worldcup, name='worldcup'),
    path('worldcupLogic/', views.WorldcupLogic, name='worldcupLogic'),
]