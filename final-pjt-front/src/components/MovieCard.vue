<template>
    <div v-if="movie">
        {{movie}}
        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`">
        <p>제목 : {{movie.title }}</p>
        <p>개봉일 : {{movie.release_date}}</p>
        <div>
            <button
            @click="goPostReview(movie)"
            >리뷰 작성하기</button>
            <button
            
            @click="likeMovie"
            >좋아요</button>
            {{like_users_count}}
        </div>
    </div>                
</template>

<script>
import axios from 'axios'
const DJANGO_URL='http://127.0.0.1:8000'


export default {
    name:'MovieCard',
    props: {
        movie:Object,
    },
    data() {
        return {
        user_id: this.$store.state.user_id,
        like_users_count: this.movie.like_users.length,
        like_users: this.movie.like_users,
        isLike: this.movie.like_users.some( user => this.user_id === user.id ),
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
                console.log(res.data.like_users)
            })
            .catch(() => { })
    },

    },

}
</script>

<style>

</style>