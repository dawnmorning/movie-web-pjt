from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.user_ru, name='user_ru'),
    path('follow/<str:username>/', views.follow, name='follow'),
]