<template>
  <div>

<!-- 최신순 영화 -->
    <div>
        <h1>최신순</h1>
        <button
        @click="latest_count ++"
        >더보기</button>
        <section class='please'>
            <div 
            v-if='latestMovies'
            class="container"
            >
                <div v-for='movie in latestMovies'
                    :key='movie.id'
                    >
                    <div>
                        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`">
                        <p>제목 : {{movie.title }}</p>
                        <p>개봉일 : {{movie.release_date}}</p>
                        <div>
                            <button
                            @click="goPostReview(movie)"
                            >리뷰 작성하기</button>
                            <button>좋아요</button>
                        </div>
                    </div>                
                </div>        
            </div>
        </section>
    </div>
<!-- 인기순 영화 -->
    <div>
        <h1>인기순</h1>
        <button
        @click="popular_count ++"
        >더보기</button>
        <section class='please'>
            <div 
            v-if='popularMovies'
            class="container"
            >
                <div v-for='movie in popularMovies'
                    :key='movie.id'
                    >
                    <div>
                        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`">
                        <p>제목 : {{movie.title}}</p>
                        <p>개봉일 : {{movie.release_date}}</p>
                    </div>                
                </div>        
            </div>
        </section>
    </div>
<!-- 평점순 영화 -->
    <div>
        <h1>평점순</h1>
        <button
        @click="vote_count ++"
        >더보기</button>
        <section class='please'>
            <div 
            v-if='voteMovies'
            class="container"
            >
                <div v-for='movie in voteMovies'
                    :key='movie.id'
                    >
                    <div>
                        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`">
                        <p>제목 : {{movie.id}}</p>
                        <p>제목 : {{movie.title}}</p>
                        <p>개봉일 : {{movie.release_date}}</p>
                    </div>                
                </div>        
            </div>
        </section>
    </div>
<!-- 랜덤 영화 -->
    <div>
        <h1>랜덤</h1>
        <button
        @click="getRandomMovies"
        >더보기</button>
        <section class='please'>
            <div
            v-if='randomMovies'
            class="container"
            >
                <div v-for='movie in randomMovies'
                    :key='movie.id'
                    >
                    <div>
                        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`">
                        <p>제목 : {{movie.title }}</p>
                        <p>개봉일 : {{ movie.release_date }}</p>
                    </div>                
                </div>        
            </div>
        </section>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'


const DJANGO_URL='http://127.0.0.1:8000'
// const IMG_URL = "https://image.tmdb.org/t/p/w500"
export default {
    name: 'RecommenDation',
    components:{
    
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
        goPostReview(movie) {
            this.$router.push({ name: 'PostReview', params:{ movie_id: movie.id, movie: movie}})
        },         
    },

    created(){
        this.$store.dispatch('getMovies')
        this.getRandomMovies()
    }
}   
</script>

<style>
.container{
    /* width: 90%; */
    display: grid;
    /* grid-template-areas: 1fr 1fr 1fr 1fr 1fr 1fr; */
    grid-template-columns: repeat(10, 1fr);
    /* grid-auto-rows: 300px; */
    /* grid-auto-flow: column; */
    /* grid-auto-columns: 1fr 1fr 1fr; */
    /* grid-template-rows: repeat(3, 1fr); */
    grid-gap: 50px;
    /* grid-template-columns: 100px 100px 100px; */
    width : 1600px;
    margin-top: 100px;
    
}
.please{
    display: flex;
    justify-content: center;
} 
</style>