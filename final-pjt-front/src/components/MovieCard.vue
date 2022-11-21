<template>
    <div v-if="movie">
        <!-- {{movie}} -->
        
        <div>
            <button
            @click="goPostReview"
            >리뷰 작성하기</button>
            <button @click="likeMovie">
                <span v-if="!isLike">좋아요</span>
                <span v-if="isLike">좋아요 취소</span>    좋아요
            </button>
            {{like_users_count}}
            <div v-if="like_users">
                <h6>좋아요 누른 사람</h6>
                <ul v-for="like_user in like_users" :key="like_user.id">
                    <img :src="`http://127.0.0.1:8000${like_user.profile_image}`" alt="프로필 이미지">
                   <router-link :to="{name: 'ProfileView', params: { username : like_user.username}}">
                        {{like_user.nickname}}
                    </router-link>
                </ul>

            <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class='gridimage animate__animated animate__jackInTheBox'>
            <div 
            class='hoverbtn animate__animated animate__fadeInUp' style=''>
                <button
                @click="goPostReview(movie)"
               
                class='w-btn w-btn-blue '
                >리뷰 작성하기</button>
                <button
                @click="likeMovie"
                
                class= 'fun-btn'
                >좋아요</button>
                {{like_users_count}}
                {{like_users}}
            </div>
        </div>
        
     
        <!-- <p>제목 : {{movie.title }}</p>
        <p>개봉일 : {{movie.release_date}}</p> -->
       
    </div>                
</template>

<script>
import axios from 'axios'
const DJANGO_URL='http://127.0.0.1:8000'


export default {
    name:'MovieCard',
    components:{
        // Carousel,
        // Slide
    },
    props: {
        movie:Object,
    },
    data() {
        return {
            // is_focus: false,  blur/focus 함수 할때 써먹을용 삭제 x -종혁
    }
    },
    methods: {
        goPostReview(movie) {
            this.$router.push({ name: 'PostReview', params:{ movie_id: movie.id, movie: movie}})
        },
        likeMovie(){
            axios({
                method: 'put',
                url: `${DJANGO_URL}/api/v2/movies/like/${this.movie.id}/`,
                headers: { Authorization : `Token ${this.$store.state.token}` }
            })
            .then((res) => {
                this.isLike = res.data.isLike,
                this.like_users_count = res.data.count
                this.like_users = res.data.like_users
            })
            .catch(() => {})
    },

    },

}
</script>


<style>

.gridimage{
     object-fit: cover;
     height: 750px;
     /* margin-bottom: -40px; */
     margin-top: 30px;
     width: 246px;
     height: 355px;
}


.color-bg-start {
  background-color: salmon;
}
.hoverbtn{
    display:none;
    text-align: center;
    /* align-items: center; */
    margin-top: -30px;
}
img:hover +.hoverbtn{
    display: block;
}
.hoverbtn:active{
    display:block;
    cursor: pointer;
}

/* toggle class bg-animate-color */

.bg-animate-color {
  animation: random-bg .5s linear infinite;
}


/* add animation to bg color  */

@keyframes random-bg {
  from {
    filter: hue-rotate(0);
  }
  to {
    filter: hue-rotate(360deg);
  }
}

.fun-btn {
  /* change bg color to get different hues    */
  background-color: salmon;
  color: white;
  /* padding: 2em 3em; */
  border: none;
  transition: all .3s ease;
  border-radius: 5px;
  letter-spacing: 2px;
  text-transform: uppercase;
  outline: none;
  align-self: center;
  cursor: pointer;
  font-weight: bold;
  width:118px;
  height:30px;
    border-radius: 15px;

}

.fun-btn:hover {
  animation: random-bg .5s linear infinite, grow 1300ms ease infinite;
}

.start-fun {
  background-color: #fff !important;
  /* change color of button text when fun is started   */
  color: salmon !important;
}

/* pulsating effect on button */
@keyframes grow {
  0% {
    transform: scale(1);
  }
  14% {
    transform: scale(1.3);
  }
  28% {
    transform: scale(1);
  }
  42% {
    transform: scale(1.3);
  }
  70% {
    transform: scale(1);
  }
}

/* 작성하기 버튼 */
.w-btn {
    position: relative;
    border: none;
    display: inline-block;
    /* padding: 15px 30px; */
    border-radius: 15px;
    font-family: "paybooc-Light", sans-serif;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    text-decoration: none;
    font-weight: 600;
    transition: 0.25s;
}
.w-btn-blue {
    background-color: #6aafe6;
    color: #d4dfe6;
}
</style>