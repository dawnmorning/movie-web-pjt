from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from movies.models import Movie
from .models import Review, Comment
from .serializers import ReviewSerializer,CommentSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reviews(request):
    # 리뷰수가 많은 상황을 대비하여 Paginator 사용
    try:
        page = int(request.GET.get('page'))
        reviews_list = Review.objects.all().order_by('-created_at')
        paginator = Paginator(reviews_list, 5, allow_empty_first_page = True)
        reviews = paginator.page(page)

        serializer = ReviewSerializer(data=reviews, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    except:
        return Response({'message': '게시글이 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_c(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    serializer = ReviewSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user = request.user)
        return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def review_u(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.user != review.user:
        return Response({'message': '해당 작업의 권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    serializer = ReviewSerializer(review, data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def review_d(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.user != review.user:
        return Response({'message': '해당 작업의 권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    review.delete()
    return Response({'message':f'리뷰 {review_pk}번 글이 삭제되었습니다.'}, status= status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_like(request,review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user

    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
        is_like = False
    else:
        review.like_users.add(user)
        is_like = True
    context ={
        'is_like':is_like,
        'count': review.like_users.count(),
    }
    return Response(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_c(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
   
    serializer = CommentSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user = request.user)
        return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_d(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.user != comment.user:
        return Response({'message': '해당 작업의 권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    comment.delete()
    return Response({'message':f'댓글 {comment_pk}번 글이 삭제되었습니다.'}, status= status.HTTP_204_NO_CONTENT)


# 댓글에 하트 표시
@api_view(['POST'])
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
    context ={
        'is_like': is_like,
        'count':comment.like_users.count(),
    }
    return Response(context)