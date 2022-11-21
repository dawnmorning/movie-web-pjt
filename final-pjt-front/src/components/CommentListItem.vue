<template>
  <div  v-if="comment">
    <hr>
    {{comment}}
    {{ comment.author.nickname }} |
    {{ comment.content }}
    <button
    @click="deleteComment"
    >X</button>

    
  </div>
</template>
<script>
// const DJANGO_URL='http://127.0.0.1:8000'
// import axios from 'axios'

// { "id": 10,
//  "author": { "id": 1, "username": "lwi995", "email": "lwi995@naver.com", "nickname": "211", "profile_image": "/media/default.jpg", "grade": 0, "followings": [ { "id": 3, "username": "admin", "nickname": "이원일1", "profile_image": "/media/default.jpg", "grade": 0, "followings": [] } ], "followers": [], "cnt_followings": 1, "cnt_followers": 0 }, 
// "like_users": [], 
// "cnt_like_users": 0, 
// "content": "dsfsadsfdsdasdsa", 
// "review": 7 }

export default {
  name:'CommentListItem',
  props: {
      comment: Object,
  },
  data() {
    return {
      user_id : this.$store.state.user_id,
      comment_like_users: this.comment.like_users,
      comment_like_users_count: this.comment.cnt_like_users,
      comment_isLike: null,
      created_at:null,
    }
  },
  methods: {
    deleteComment() {            
      this.$store.dispatch('deleteComment', this.comment)
    },
    // getComment() {
    //   console.log(this.comment)
    //   axios({
    //     url:`${DJANGO_URL}/api/v3/comment/${this.comment.id}/`,
    //     headers:{ Authorization : `Token ${this.$store.state.token}`,},
    //   })
    //   .then(res => {
    //     // this.comment = res.data
    //     this.comment_like_users = res.data._like_users
    //     this.comment_like_users_count = res.data.cnt_like_users
    //     this.comment_like_users_count = res.data.like_users.some(like_user => { return like_user.id === this.user_id })
    //     this.created_at = res.data.created_at
    //   })
    // },
    // watch: {
    //   review(value) {
    //     console.log(value)
        
    //   }
    // }
  },
  mounted() {
    console.log(this.comment)
    
    // this.getComment()
  }

}
</script>

<style>

</style>