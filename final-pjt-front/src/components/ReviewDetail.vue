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
            
        </div>
        </div>
        
    </div>
</template>
<script>

export default {
    name: 'ReviewDetail',
    
    computed: {
        review() {
            return this.$route.query?.review
        }
    },
}
</script>

<style>

</style>