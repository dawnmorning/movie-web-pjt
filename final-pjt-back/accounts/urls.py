from django.urls import path
from .views import Profile_RU

urlpatterns = [
    path('profile/<str:username>/', Profile_RU, name='Profile'),
]