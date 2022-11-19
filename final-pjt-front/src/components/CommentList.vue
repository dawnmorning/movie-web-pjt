<template>
  <div v-if='comments'>
    <div v-for="comment in comments" :key="comment.id">
        <CommentListItem
        :comment="comment"
        />
    </div>
  </div>
</template>

<script>
// const DJANGO_URL='http://127.0.0.1:8000'
// import axios from 'axios'
import CommentListItem from '@/components/CommentListItem'

export default {
    name: 'CommentList',
    props: {
        comments:Array,
    },
<<<<<<< HEAD
    methods: {
        deleteComment(comment) {
            axios({
                method : 'delete',
                url : `${DJANGO_URL}/api/v3/comment/delete/${comment.id}/`,
                headers:{
                    Authorization : `Token ${this.$store.state.token}`,
                },
            })
            // .then(res => console.log(res))
            // .catch(err => console.log(err))
        }
=======
    components: {
        CommentListItem
>>>>>>> develop1
    }
}
</script>

<style>

</style>