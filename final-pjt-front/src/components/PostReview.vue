<template>
    <div>
        <div v-if="movie">
            <p>{{movie.title}}</p>
            <p>{{movie.poster_path}}</p>
            <p>{{movie.overview}}</p>
            <p>{{movie.vote_average}}</p>
        </div>
        <div>
            <div>title: <input type="text" value="Title" v-model.trim="title"></div>
            <div>content: <input type="text" value="content" v-model.trim="content"></div>
            <div>rating: <input type="number" value="rating" v-model.trim="rating"></div>
            <button @click='postReview'>post</button>
        </div>
    </div>

</template>

<script>

export default {
    name: 'PostReview',
    data() {
        return {
            // movie:null,
            title:null,
            content:null,
            rating:null,
        }
    },
    computed: {
        movie() {
            return this.$store.state.movie_detail
        }
    },
    methods: {
        postReview() {
            if ( this.title && this.content && this.rating ) {
                const payload = {
                    title: this.title,
                    content: this.content,
                    rating: this.rating,
                    movie_id: this.movie.id,
                }
                this.$store.dispatch('postReview', payload)
            }
            else { alert('빈 칸을 채워주세요.') }
        },
    },
    created() {
        const payload = {
            backTo : 'PostReview',
            movie_id: this.$route.params.movie_id,
        }
        this.$store.dispatch('getMovieDetail', payload)
    }
}
</script>

<style>

</style>