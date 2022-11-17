from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import GenreMoviegenreSerializer
# Create your views here.
import time
import random
import requests
from .models import Genre, WorldcupLogic
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer, WorldcupLogicSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Worldcup(request):
    movielist = []
    if request.method == 'GET':
        genres = Genre.objects.all()    # 장르 인스턴스 생성
        for genre in genres:
            movies_by_genre = genre.movies.order_by('-vote_average')[:10]   # 장르별 평점 역순
            while True:
                movie_by_genre = movies_by_genre[random.randrange(0, 10)]   # 장르별 평점 상위 영화 10 개 중 한 개 추출해서 대표 영화로 선정
                if movie_by_genre in movielist:                             # 영화가 겹치는 경우 피하기
                    continue
                movielist.append(movie_by_genre)
                break
        serializer = MovieSerializer(data=movielist, many=True)
        print(serializer.is_valid())
        return Response(serializer.data)    

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def WorldcupLogic(request):

#     if request.method == 'POST':

