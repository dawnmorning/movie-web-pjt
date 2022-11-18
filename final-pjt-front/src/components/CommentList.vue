<template>
  <div v-if='comments'>
    <div v-for="comment in comments" :key="comment.id">
        <hr>
        {{ comment.author }} |
        {{ comment.content }}
        <button
        @click="deleteComment(comment)"
        >X</button>
    </div>
  </div>
</template>

<script>
const DJANGO_URL='http://127.0.0.1:8000'
import axios from 'axios'
export default {
    name: 'CommentList',
    props: {
        comments:Array,
    },
    methods: {
        deleteComment(comment) {
            axios({
                method : 'delete',
                url : `${DJANGO_URL}/api/v3/comment/delete/${comment.id}/`,
                headers:{
                    Authorization : `Token ${this.$store.state.token}`,
                },
            })
            .then(res => console.log(res))
            .catch(err => console.log(err))
        }
    }
}
</script>

<style>

</style>