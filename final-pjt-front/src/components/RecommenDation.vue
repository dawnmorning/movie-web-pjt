<template>
    <div>
<!-- 최신순 영화 -->

        <div class='new col-md '>
            <div class='jua position-relative ' style='margin-top:30px; right:30%; top:100px; '>
                <span style='margin-bottom:5px; margin-top:20px; fw-lighter'>최근 개봉한 영화</span>
                <span><button
                @click="latest_count ++"
                style='font-size:20px; top:-5px; '
                class='position-relative btn btn-outline-primary'
                >더보기</button></span>
            </div>
            <div>
                
                <div v-if='latestMovies' class='update justify-content-center' >
                    <div v-for='movie in latestMovies' :key='movie.id' style='margin-top:-20px; margin-right:5px; '> 
                        <MovieCard :movie="movie"/>
                    </div>        
                </div>
            </div>
        </div>
        
<!-- 인기순 영화 -->
        <div class='popular'>
            <div class='jua position-relative' style='margin-top:30px; right:30%; top:100px;'>
            <span style='margin-bottom:5px; margin-top:10px;'>지금, 인기있는 영화</span>
            <button
            @click="popular_count ++"
            style='font-size:20px; top:-5px; '
            class='position-relative btn btn-outline-primary'
            >더보기</button>
            </div>
            <div class=''>
                <div  v-if='popularMovies' class='update justify-content-center' >
                    <div v-for='movie in popularMovies' :key='movie.id' style='margin-right:5px;'>
                        <MovieCard :movie="movie"/>
                    </div>        
                </div>
            </div>
        </div>
<!-- 평점순 영화 -->
        <div class='voteaver'>
            <div class='jua position-relative' style='margin-top:30px; right:30%; top:100px;'>
            <span style='margin-bottom:5px; margin-top:10px;'>평점이 높은 영화</span>
                <button
                @click="vote_count ++"
                style='font-size:20px; top:-5px; '
                class='position-relative btn btn-outline-primary'
                >더보기</button>
            </div>
            <div class=''>
                <div  v-if='voteMovies' class='update justify-content-center' >
                    <div v-for='movie in voteMovies' :key='movie.id' style='margin-right:5px;'>
                        <MovieCard :movie="movie"/>

                    </div>        
                </div>
            </div>
        </div>
        <!-- 랜덤 영화 -->   
        <div class='random' >
            <div class='jua position-relative' style='margin-top:30px; right:30%; top:100px;'>
            <span style='margin-bottom:5px; margin-top:10px; position:relative; right:60px;'>랜덤 영화</span>
                <button
                @click="getRandomMovies"
                style='font-size:20px; top:-5px; right:50px;'
                class='position-relative btn btn-outline-primary'
                >더보기</button>
            </div>
            <div class=''>
                <div  v-if='randomMovies' class='update justify-content-center' >
                    <div v-for='movie in randomMovies' :key='movie.id' style='margin-right:5px;'>
                        <MovieCard :movie="movie"/>
    
                    </div>        
                </div>
            </div>
<!--         
            <div class='jua position-relative' style='margin-top:30px; right:30%; top:100px;'>
            <span style='margin-bottom:5px; margin-top:10px;'>랜덤 추천</span>
                <button
                @click="getRandomMovies"
                style='font-size:20px; top:-5px;'
                class='position-relative btn btn-outline-success'
                >더보기</button>
            </div>
            <div class=''>
                <div  v-if='randomMovies' class='update' >
                    <carousel :per-page="9" :navigate-to="someLocalProperty" :mouse-drag="false">
                        <slide v-for='movie in randomMovies' :key='movie.id' class='slide__item '>
                            <MovieCard  :movie="movie"/>
                        </slide>
                    </carousel>
                </div>
            </div> -->
        </div>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'
import MovieCard from '@/components/MovieCard'
// import { Carousel, Slide } from 'vue-carousel';
const DJANGO_URL='http://127.0.0.1:8000'
// const IMG_URL = "https://image.tmdb.org/t/p/w500"
export default {
    name: 'RecommenDation',
    components:{
        MovieCard,
        // Carousel,
        // Slide
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
        latest_count(value) {{ this.latest_count = value % 20 }},
        popular_count(value) {{ this.popular_count = value % 20 }},
        vote_count(value) {{ this.vote_count = value % 20 }},
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
    display: grid;
    /* grid-template-areas: 1fr 1fr 1fr 1fr 1fr 1fr; */
    grid-template-columns: repeat(5, 1fr);
    /* grid-auto-rows: 300px; */
    /* grid-auto-flow: column; */
    /* grid-auto-columns: 1fr 1fr 1fr; */
    /* grid-template-rows: repeat(3, 1fr); */
    /* grid-gap: 50px; */
    /* grid-template-columns: 100px 100px 100px; */
    /* width : 400px; */
    margin-top: 100px;
    grid-gap: -90px; 
    width: 70%;
    text-align: center;
    left: 13%;
    position: relative;
}

</style>