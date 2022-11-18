from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from movies.models import Movie
from .models import Review, Comment
from .serializers import ReviewSerializer,CommentSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

# Create your views here.


# def reviews(request):
#     # 리뷰수가 많은 상황을 대비하여 Paginator 사용
#     page = int(request.GET.get('page'))
#     reviews = Review.objects.all().prefetch_related('comment_set')
#     print(reviews)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_c(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    serializer = ReviewSerializer(data =request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user = request.user)
        return Response(serializer.data, status= status.HTTP_201_CREATED)

