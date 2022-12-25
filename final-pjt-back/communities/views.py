

from movies.models import Movie
from .models import Review, Comment
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import ReviewSerializer,CommentSerializer
from accounts.serializers import NestedUserSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

User = get_user_model()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reviews(request):
    # 리뷰수가 많은 상황을 대비하여 Paginator 사용
    reviews = Review.objects.all().order_by('-created_at')
    serializer = ReviewSerializer(data=reviews, many=True)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_reviews(request, username):
    # 리뷰수가 많은 상황을 대비하여 Paginator 사용
    user = get_object_or_404(User, username=username)
    my_reviews = user.reviews.all().order_by('-created_at')
    serializer = ReviewSerializer(data=my_reviews, many=True)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def review_r(request, review_pk):
    # 리뷰수가 많은 상황을 대비하여 Paginator 사용
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_c(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def review_u(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.user != review.author:
        return Response({'message': '해당 작업의 권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def review_d(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.user != review.author:
        return Response({'message': '해당 작업의 권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    review.delete()
    return Response({'review_id': review_pk}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user

    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        is_like = False
    else:
        review.like_users.add(user)
        is_like = True

    like_users = review.like_users.all()
    serializer = NestedUserSerializer(data=like_users, many=True)
    serializer.is_valid()
    
    context = {
        'is_like': is_like,
        'count': review.like_users.count(),
        'like_users': serializer.data,
    }
    return Response(context)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_ru(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_c(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
   
    serializer = CommentSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_d(request, comment_pk):
    comment = get_object_or_404(Comment, id=comment_pk)
    
    if request.user != comment.author:
        return Response({'message': '해당 작업의 권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    comment.delete()
    return Response({'comment_pk':comment_pk}, status=status.HTTP_204_NO_CONTENT)


# 댓글에 하트 표시
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def comment_like(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user

    if comment.like_users.filter(pk=user.pk).exists():
        comment.like_users.remove(user)
        is_like = False
    else:
        comment.like_users.add(user)
        is_like = True

    like_users = comment.like_users.all()
    serializer = NestedUserSerializer(data=like_users, many=True)
    serializer.is_valid()
    context = {
        'is_like': is_like,
        'count': comment.like_users.count(),
        'like_users': serializer.data,
    }
    return Response(context)