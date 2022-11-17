import time
import requests
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer
from apscheduler.schedulers.background import BackgroundScheduler

TMDB_KEY = "931f9fa88e1e198f309e60e64a0f2062"

def getMOVIES():
    print(f'******{time.strftime("%H:%M:%S")}******')

    TMDB_URL = "https://api.themoviedb.org/3/genre/movie/list"
    response = requests.get(TMDB_URL, params={"api_key":TMDB_KEY, "language":'ko-KR'}).json()
    genres = response['genres']
    for genre in genres:
        genre_id = genre['id']
        genre['genre_id'] = genre_id
        serializer = GenreSerializer(data=genre)
        if serializer.is_valid():
            serializer.save()
    
    print('get gernes completed')
    print(f'******{time.strftime("%H:%M:%S")}******')

    # TMDB_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_KEY}&language=ko-KR&sort_by=release_date.asc&include_adult=false&include_video=true&page=1&with_watch_monetization_types=flatrate"
    TMDB_URL = "https://api.themoviedb.org/3/movie/popular"

    # 영화 갯수는 755037
    results = []

    for page in range(1, 501):

        params = {
            "api_key":TMDB_KEY,
            "language":'ko-KR',
            "page":page,
        }

        response_MOVIE = requests.get(TMDB_URL, params=params).json()
        results += response_MOVIE['results']
    
    # 만 개 데이터
    print(len(results))
    # 더 필요한 정보를 movie detail api에서 보충하기
    genre_ids = {}

    for result in results:
        movie_id = result['id']

        result['movie_id'] = movie_id
        movie = Movie.objects.filter(movie_id=movie_id)
        if len(movie) != 0:
            continue

        genre_ids[movie_id] = result['genre_ids']

        movieSerializer = MovieSerializer(data=result)
        if movieSerializer.is_valid():
            movieSerializer.save()
        else:
            pass
            

    # # 무비_장르 N:M테이블 채우기
    for movie_id, values in genre_ids.items():
        
        if Movie.objects.filter(movie_id=movie_id).exists():
            movie = Movie.objects.get(movie_id=movie_id)
            for genre_id in values:
                
                genre = Genre.objects.get(genre_id=genre_id)
                movie.genres.add(genre)
        
    print('===================')
                
def main():
    sched = BackgroundScheduler(timezone='Asia/Seoul')
    
    # sched.add_job(getMOVIES, 'cron', minute="58",second="10", id='getMOVIES')
    sched.start()
    # classapscheduler.triggers.interval.IntervalTrigger(weeks=0, days=0, hours=0, 