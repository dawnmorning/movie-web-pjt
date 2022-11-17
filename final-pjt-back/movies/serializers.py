from .models import Movie, Genre, Worldcup, WorldcupLogic
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

# 영화별 장르를 movie-genre테이블에 저장하는 시리얼라이저
class GenreMoviegenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = 'movies'

class WorldcupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worldcup
        fields = "__all__"

# 월드컵 결과에 따른 추천 시리얼라이져
class WorldcupLogicSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = WorldcupLogic
        read_only_fields = 'user,'