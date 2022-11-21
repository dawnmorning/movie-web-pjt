<template>
    <div v-if="movie">
        {{movie}}
        <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`">
        <p>제목 : {{movie.title }}</p>
        <p>개봉일 : {{movie.release_date}}</p>
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

            </div>
        </div>
    </div>                
</template>

<script>
import axios from 'axios'
const DJANGO_URL='http://127.0.0.1:8000'


export default {
    name:'MovieCard',
    props: {
        movie_id:Number,
    },
    data() {
        return {
            user_id: this.$store.state.user_id,
            movie: null,
            like_users_count: null,
            like_users: null,
            isLike: null,
        }
    },
    methods: {
        goPostReview() {
            this.$router.push({ name: 'PostReview', params:{ movie_id: this.movie.id, movie: this.movie}})
        },
        likeMovie() {
            axios({
                method: 'put',
                url: `${DJANGO_URL}/api/v2/movies/like/${this.movie.id}/`,
                headers: { Authorization : `Token ${this.$store.state.token}` },
            })
            .then(res => {
                this.isLike = res.data.isLike,
                this.like_users_count = res.data.count
                this.like_users = res.data.like_users
            })
        },
        getMovie() {
            axios({
                method: 'get',
                url: `${DJANGO_URL}/api/v2/${this.movie_id}/movies/`,
                headers: { Authorization : `Token ${this.$store.state.token}` }
            })
            .then(res => {
                const data = res.data
                this.movie = res.data
                this.isLike = data.like_users.some(user => { return user.id === this.user_id })
                this.like_users_count = data.cnt_like_users
                this.like_users = data.like_users       
            })
            .catch(err => { console.log(err) })
        }
    },
    created(){
        this.getMovie()
    }

}
</script>

<style>

</style>