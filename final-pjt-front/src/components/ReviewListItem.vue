<template>
  <div>
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
  </div>
</template>
<script>
import CommentList from '@/components/CommentList'
// const IMG_URL = "https://image.tmdb.org/t/p/w500"

export default {
    name: 'ReviewListItem',
    data() {
        return {
            inputData: null,
        }
    },
    components: {
        CommentList,
    },
    props:{
        review:Object,
    },
    // computed: {
    //     comments() {
    //         return this.review.comments
    //     }
    // },
    methods: {
        createComment() {
            const payload = {
                review_id: this.review.id,
                comment: this.inputData,
            }
            this.$store.dispatch('createComment', payload)
            this.inputData = null

        }
    },
    created() {
        // console.log(this.review.comments)
        // console.log(this.review.movie)
    }
}
</script>

<style>

</style>