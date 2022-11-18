<template>
  <div>
    <div class="card">
        <div class="card-body">
        <h5 class="card-title">영화 : {{review.movie.title}}</h5>
        <div><img :src='`https://image.tmdb.org/t/p/w500/${review.movie.poster_path}`'></div>       
        
        <hr>
        <div class="card-body">
        <h5 class="card-title">리뷰 : {{review.title}}</h5>
        <h5 class="card-subtitle mb-2 text-muted">{{review.updated_at}}</h5>
        <h5 class="card-subtitle mb-2 text-muted">별점 : {{review.rating}}</h5>
        <p class="card-text">작성자 : {{review.user}}</p>
        <p class="card-text">{{review.content}}</p>
        </div>
        
        <!-- 댓글 -->
        <CommentList
        :comments=review.comments
        />

        
    </div>
    </div>
    
  </div>
</template>
<script>
import CommentList from '@/components/CommentList'
// const IMG_URL = "https://image.tmdb.org/t/p/w500"

export default {
    name: 'ReviewListItem',
    components: {
        CommentList,
    },
    props:{
        review:Object,
    },
    created() {
        // console.log(this.review.comments)
        // console.log(this.review.movie)
    }
}
</script>

<style>

</style>