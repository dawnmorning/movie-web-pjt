from django.urls import path
from . import views

# api/v1/
urlpatterns = [
    path('<str:username>/', views.user_ru, name='user_ru'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('users/all/', views.users_r, name='users_r'),
]