from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile_ru, name='profile_ru'),
]