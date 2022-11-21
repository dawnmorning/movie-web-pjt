<template>
  <div>
    <hr>
    {{ comment.author.nickname }} |
    {{ comment.content }}
    <button
    @click="deleteComment(comment)"
    >X</button>

    
  </div>
</template>
<script>
const DJANGO_URL='http://127.0.0.1:8000'
import axios from 'axios'

export default {
    name:'CommentListItem',
    props: {
        comment_id: Number,
    },
    data() {
      return {
        user_id : this.$store.state.user_id,
        comment: null,
        comment_like_users: null,
        comment_like_users_count: null,
        comment_isLike: null,
        created_at:null,
      }
    },
    methods: {
        deleteComment(comment) {            
          this.$store.dispatch('deleteComment', comment)  
        },
        getComment() {
          axios({
            url:`${DJANGO_URL}/api/v3/comment/${this.comment_id}/`,
            headers:{ Authorization : `Token ${this.$store.state.token}`,},
          })
          .then(res => {
            this.comment = res.data
            this.comment.comment_like_users = res.data.comment_like_users
            this.comment.comment_like_users_count = res.data.comment_like_users.comment_like_users
            this.comment.comment_like_users_count = res.data.like_users.some(like_user => { return like_user.id === this.user_id })
            this.created_at = res.data.created_at
            console(res)
          })
        }
    },
    beforeCreate() {
      this.getComment()
    }

}
</script>

<style>

</style>