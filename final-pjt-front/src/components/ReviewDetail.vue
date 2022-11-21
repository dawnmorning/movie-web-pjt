<template>
    <div v-if="review">
        <div class="card">
            <p class="card-text">작성자 : {{review.author}}</p>
            <div class="card-body">
                <div><img :src='`https://image.tmdb.org/t/p/w500/${review.movie.poster_path}`'></div>
                <hr>       
                <h5 class="card-title">영화 : {{review.movie.title}}</h5>
            
                <hr>
                <div class="card-body">
                <h5 class="card-title">리뷰 : {{review.title}}</h5>
                <h5 class="card-subtitle mb-2 text-muted">{{review.updated_at}}</h5>
                <h5 class="card-subtitle mb-2 text-muted">별점 : {{review.rating}}</h5>
                <p class="card-text">{{review.content}}</p>
                </div>
                       <!-- 댓글 -->
                <CommentList
                :comments=review.comments
                />

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
        </div>
        <button @click="goBack">뒤로가기</button>
    </div>
</template>
<script>
// import axios from 'axios'
// const DJANGO_URL='http://127.0.0.1:8000'
import CommentList from '@/components/CommentList'

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
        }
    },
    components: {
        CommentList,
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