<template>
  <div>

<!-- 최신순 영화 -->
    <div class='new'>
        <div class='jua' style='margin-top:80px;'>
            <h1 style='margin-bottom:5px; margin-top:20px;'>최근 개봉한 영화</h1>
            <button
            @click="latest_count ++"
            style='font-size:20px; margin-top:20px;'
            >더보기</button>
        </div>
        <div>
            <div  v-if='latestMovies' class='update' >
                
                
                 <div v-for='movie in latestMovies' :key='movie.id' style='margin-top:-20px;'> 
                    <MovieCard :movie="movie.id"/>
                
                </div>        
            </div>
        </div>
    </div>
    
<!-- 인기순 영화 -->
    <div class='popular'>
        <div class='jua' style='margin-top:80px;'>
        <h1 style='margin-bottom:5px; margin-top:20px;' >지금, 인기있는 영화</h1>
        <button
        @click="popular_count ++"
        style='font-size:20px; margin-top:20px;'
        >더보기</button>
        </div>
        <div class=''>
            <div  v-if='popularMovies' class='update' >
                <div v-for='movie in popularMovies' :key='movie.id'>
                    <MovieCard :movie_id="movie_id"/>
                </div>        
            </div>
        </div>
    </div>
<!-- 평점순 영화 -->
    <div class='voteaver'>
        <div class='jua' style='margin-top:80px;'>
            <h1 style='margin-bottom:5px; margin-top:20px;'>평점순</h1>
            <button
            @click="vote_count ++"
            style='font-size:20px; margin-top:20px;'
            >더보기</button>
        </div>
        <div class=''>
            <div  v-if='voteMovies' class='update' >
                <div v-for='movie in voteMovies' :key='movie.id'>
                    <MovieCard :movie_id="movie.id"/>

                </div>        
            </div>
        </div>
    </div>
<!-- 랜덤 영화 -->
    <div>
        <h1>랜덤</h1>
        <button
        @click="getRandomMovies"
        >더보기</button>
        <section class='please'>
            <div  v-if='randomMovies' class="container" >
                <div v-for='movie in randomMovies' :key='movie.id'>
                    <MovieCard :movie_id="movie.id"/>
                </div>        
    <div class='random' >
        <div class='jua' style='margin-top:80px;'>
            <h1 style='margin-bottom:5px; margin-top:20px;'>랜덤</h1>
            <button
            @click="getRandomMovies"
            style='font-size:20px; margin-top:20px;'
            >더보기</button>
            
        </div>
        <div class=''>
            <div  v-if='randomMovies' class='update' >
                <carousel :per-page="9" :navigate-to="someLocalProperty" :mouse-drag="false">
                    <slide v-for='movie in randomMovies' :key='movie.id' class='slide__item '>
                <!-- <div v-for='movie in randomMovies' :key='movie.id'> -->
                    <MovieCard  :movie="movie.id"/>
                    </slide>
                </carousel>
                <!-- </div>         -->
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'
import MovieCard from '@/components/MovieCard'
import { Carousel, Slide } from 'vue-carousel';
const DJANGO_URL='http://127.0.0.1:8000'
// const IMG_URL = "https://image.tmdb.org/t/p/w500"
export default {
    name: 'RecommenDation',
    components:{
        MovieCard,
        Carousel,
        Slide
    },
    data(){
        return{
            latest_count : 0,
            popular_count : 0,
            vote_count : 0,
            randomMovies : null,
            
        }
    },
    watch: {
        latest_count(value) {{ this.latest_count = value % 10 }},
        popular_count(value) {{ this.popular_count = value % 10 }},
        vote_count(value) {{ this.vote_count = value % 10 }},
    },
    computed: {
        latestMovies() {
            const fr = this.latest_count
            return this.$store.state.latest_movies.slice(fr * 10, fr * 10 + 10)
        },
        popularMovies() {
            const fr = this.popular_count
            return this.$store.state.popular_movies.slice(fr * 10, fr * 10 + 10)
        },
        voteMovies() {
            const fr = this.vote_count
            return this.$store.state.vote_movies.slice(fr * 10, fr * 10 + 10)
        },

    },
    methods: {
        getRandomMovies(){
            axios({
                method: 'get',
                url: `${DJANGO_URL}/api/v2/movies/random/`,
                headers: { Authorization : `Token ${this.$store.state.token}` }
            })
            .then(res => {
                this.randomMovies = res.data
            })
            .catch(err => { console.log(err) })
        },     
    },

    created(){
        this.$store.dispatch('getMovies')
        this.getRandomMovies()
    }
}   
</script>

<style>

.update{
    /* width: 90%; */
    display: flex;
    /* grid-template-areas: 1fr 1fr 1fr 1fr 1fr 1fr; */
    grid-template-columns: repeat(4, auto);
    /* grid-auto-rows: 300px; */
    /* grid-auto-flow: column; */
    /* grid-auto-columns: 1fr 1fr 1fr; */
    /* grid-template-rows: repeat(3, 1fr); */
    /* grid-gap: 50px; */
    /* grid-template-columns: 100px 100px 100px; */
    /* width : 400px; */
    margin-top: 100px;
    grid-gap: -70px; 
    /* width: 70%; */
    
}

</style>