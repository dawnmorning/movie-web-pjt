<template>
    <div class='jua' style='text-align:center; margin-top:100px;' v-if="review">
        <!-- <div :style="`background-image: url(${review.movie.poster_path})`"></div> -->
        <div  class="card reviewbody " style='margin-top: 50px; font-size:20px;  width:1000px; left:25%; object-fit:cover;'>
            <p class="card-text">작성자 : {{review.author.nickname}}</p>
            <div class="card-body">
                <div><img class='img-fluid' :src='`https://image.tmdb.org/t/p/w500/${review.movie.poster_path}`'></div>
                <hr>       
                <h5 class="card-title">영화 : {{review.movie.title}}</h5>
                <hr>
                <div class="card-body" style='height:200px;'>
                    <h5 class="card-title">리뷰 : {{review.title}}</h5>
                    <h5 class="card-subtitle mb-2 text-muted">{{review.updated_at}}</h5>
                    <h5>별점 : {{review.rating}}</h5>
                    <!-- <star-rating class="card-subtitle mb-2 text-muted" :value='`${review.rating}`' :read-only='true'>별점 : {{review.rating}}</star-rating> -->
                    <p class="card-text">{{review.content}}</p>
                </div>
                
                <!-- 댓글 -->
                <div v-for="comment in comments" :key="comment.id">
                    <CommentListItem
                    :comment=comment
                    />
                </div>
                <div>
                    <hr>
                    <h5>댓글 작성하기</h5>
                    <input type="text"
                    v-model="inputData"
                    @keyup.enter="createComment" 
                    >
                    <button
                    @click="createComment"
                    >입력</button>
                </div>
            <button @click="goBack" style='font-size:20px; left:40px;'>뒤로가기</button>
            </div>
        </div>
        
    </div>
</template>
<script>
// import axios from 'axios'
// const DJANGO_URL='http://127.0.0.1:8000'
import CommentListItem from '@/components/CommentListItem'
// import StarRating from 'vue-star-rating'
export default {
    name: 'ReviewDetail',
    data() {
        return {
            inputData: null,
        }
    },
    computed: {
        review() {
            const review_id = Number(this.$route.params.review_id)
            const myReview = this.$store.state.reviews.find( function(review) {
                if (review.id === review_id) {
                    return true
                }
            })            
            return myReview
        },
        comments() {
            return this.review.comments
        }
    },
    components: {
        CommentListItem,
        // StarRating
    },
    methods: {
        goBack() {
            this.$router.push()
        },
        createComment() {
            const payload = {
                review_id: this.$route.params.review_id,
                comment: this.inputData,
            }
            this.$store.dispatch('createComment', payload)
            this.inputData = null
        },

    },
}
</script>

<style>

</style>