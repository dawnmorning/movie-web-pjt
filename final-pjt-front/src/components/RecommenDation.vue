<template>
  <div>
    <h1>Recommendation</h1>
        <button @click='showRandom'>랜덤으로 골라볼까?</button><br>

    <section class='please'>
        <div 
        v-if='movies'
        class="container"
        >
            <div v-for='(movie,idx) in movies' 
                :key='idx'
                >
                <div><img :src="movie.poster_path"></div>
                <!-- {{ movie.title }} -->
                
                <!-- {{ movie.overview}} -->
                
                <!-- {{ movie.vote_average}} -->
                
                <!-- {{ movie.poster_path}} -->
                
            </div>
            
        </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'



const DJANGO_URL='http://127.0.0.1:8000'
// const IMG_URL = "https://image.tmdb.org/t/p/w500"
export default {
    name: 'RecommenDation',
    components:{
    
    },
    data(){
        return{
            movies : [],
        }
    },
    methods:{
        showRandom(){
            axios({
                method: 'get',
                url: `${DJANGO_URL}/api/v2/movies`,
                headers: {
                  Authorization : `Token ${this.$store.state.token}`
                }
            })
                .then(res=>{
                    // console.log(res.data)
                    this.movies = res.data
                    // console.log(this.movies)
                    this.movies.forEach(movie =>{
                        movie.poster_path = "https://image.tmdb.org/t/p/w500" +movie.poster_path
                        // console.log(movie.poster_path)
                    })
                    // this.movies.forEach(movie =>{
                    //     movie.poster_path = "https://image.tmdb.org/t/p/w500" +this.movie.poster_path
                    //     console.log(movie.poster_path)
                    // })
                    // this.movies[0].poster_path = "https://image.tmdb.org/t/p/w500" +this.movies[0].poster_path
                    
                })
        }
    },
    created(){
        this.showRandom()
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