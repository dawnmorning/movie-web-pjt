from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

import time
import random

from django.db.models import Q
from accounts.models import User
from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model
from .models import Genre, Movie, WorldcupRecommend
from .serializers import MovieSerializer, WorldcupRecommendSerializer
import datetime as dt

User = get_user_model()

x = dt.datetime.now()
_today = f'{x.year}-{x.month}-{x.day}'

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movies_r(request) :
    st = time.time()
    # 상영 예정작
    movies = Movie.objects.all()
    movies1 = movies.filter(release_date__gte=_today)
    # 오늘 개봉 영화도 포함되어 있음 뷰에서 처리하기
    upcomming_movies = movies1.order_by('release_date')[:16]
    # 현재 개봉한 영화로 필터링
    movies2 = movies.filter(release_date__lte=_today)
    random_movies = movies2.order_by('?')[:16]
    latest_movies = movies2.order_by('-release_date')[:16]
    popular_movies = movies2.order_by('-popularity')[:16]
    vote_movies = movies2.order_by('-vote_average')[:16]
    
    movies_list_name = ['upcomming_movies', 'random_movies', 'latest_movies', 'popular_movies', 'vote_movies']
    movies_list = [upcomming_movies, random_movies, latest_movies, popular_movies, vote_movies]
    upcomming_serializer, random_serializer, latest_serializer, popular_serializer, vote_serializer = 0, 0, 0, 0, 0
    serializer_list = [upcomming_serializer, random_serializer, latest_serializer, popular_serializer, vote_serializer]

    context = {}
    for i in range(5):
        serializer_list[i] = MovieSerializer(data=movies_list[i], many=True)
        serializer_list[i].is_valid()
        context[movies_list_name[i]] = serializer_list[i].data
    ed = time.time()
    print(ed - st)
    return Response(context)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail_r(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def worldcup(request):
    movielist = []
    if request.method == 'GET':
        genres = Genre.objects.all()    # 장르 인스턴스 생성
        for genre in genres:
            if genre.genre_id in [37, 10770, 10751]: # 서부, TV 드라마, 가족 장르 제외
                continue

            movies_by_genre = genre.movies.order_by('-vote_average')[:10]   # 장르별 평점 역순
            while True:
                movie_by_genre = movies_by_genre[random.randrange(0, 10)]   # 장르별 평점 상위 영화 10 개 중 한 개 추출해서 대표 영화로 선정
                if movie_by_genre in movielist:                             # 영화가 겹치는 경우 피하기
                    continue
                movielist.append(movie_by_genre)
                break

        serializer = MovieSerializer(data=movielist, many=True)
        serializer.is_valid()
        return Response(serializer.data)


# 월드컵게임 결과 기반 영화 추천 알고리즘
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def worldcup_recommend(request):
    # <QueryDict: {'genre_rank1': ['28'], 'genre_rank2': ['16'], 'genre_rank3': ['53'], 'genre_rank4': ['14']}>
    user = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        # 1. 기존에 랭크 정보가 있는 경우과 없는 경우로 나누기
        if WorldcupRecommend.objects.filter(user=user).exists():                    # UPDATE
            worldcup = WorldcupRecommend.objects.get(user=user)
            serializer = WorldcupRecommendSerializer(worldcup, data=request.data)
        else:                                                                       # CREATE
            serializer = WorldcupRecommendSerializer(data=request.data)
        
        # 2. 월드컵 게임 결과 저장 및 업데이트
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)

    # 3. get 요청은 요청 사용자의 데이터가 없는 경우 처리
    elif request.method == "GET":                                               # READ
        if not WorldcupRecommend.objects.filter(user=user).exists():            # 기존 정보가 없는 경우 없음을 표현하기
            return Response({'message':' no data'})

    # 월드컵 결과에 따른 추천목록 반환
    # orm 쿼리셋 함수 활용을 통한 코드 최적화
    genre_ranks = WorldcupRecommend.objects.get(user=user)
    rank1genre = Genre.objects.get(genre_id=genre_ranks.genre_rank1)
    rank2genre = Genre.objects.get(genre_id=genre_ranks.genre_rank2)
    
    rank1movies = rank1genre.movies.all()
    filteredmovies = rank2genre.movies.all().intersection(rank1movies)
    serializer = MovieSerializer(data=filteredmovies, many=True)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)

'''
    if request.method == 'POST':
        genre_ranks = request.data
        
        # 1. 기존에 랭크 정보가 있는 경우과 없는 경우로 나누기
        if WorldcupRecommend.objects.filter(user=user).exists():
            serializer = WorldcupRecommendSerializer(user, data=request.data)
        else:
            serializer = WorldcupRecommendSerializer(data=request.data)
        
        # 2. 월드컵 게임 결과 저장 및 업데이트
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)

        # 월드컵 결과에 따른 추천목록 반환
        # orm 쿼리셋 함수 활용을 통한 코드 최적화
        rank1genre = Genre.objects.get(genre_id=int(genre_ranks['genre_rank1']))
        rank2genre = Genre.objects.get(genre_id=int(genre_ranks['genre_rank2']))

        rank1movies = rank1genre.movies.all()
        filteredmovies = rank2genre.movies.all().intersection(rank1movies)
        serializer = MovieSerializer(data=filteredmovies, many=True)
        return Response(filteredmovies)

    elif request.method == "GET":
        if WorldcupRecommend.objects.filter(user=user).exists():
            genre_ranks = WorldcupRecommend.objects.get(user=user)
            rank1genre = Genre.objects.get(genre_id=genre_ranks.genre_rank1)
            rank2genre = Genre.objects.get(genre_id=genre_ranks.genre_rank2)

            rank1movies = rank1genre.movies.all()
            filteredmovies = rank2genre.movies.all().intersection(rank1movies)
            serializer = MovieSerializer(data=filteredmovies, many=True)
            # print(serializer.is_valid())
            return Response(serializer.data)

        else:
            return Response({'message':' no data'})

'''