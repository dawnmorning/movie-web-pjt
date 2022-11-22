<template>
  <div  v-if="comment">
    <hr>

    <router-link :to="{name: 'ProfileView', params: { username : comment.author.username}}">
      <img :src="`http://127.0.0.1:8000${comment.author.profile_image}`" alt="프로필 이미지">
      {{ comment.author.nickname }}
    </router-link>
    

    | {{ comment.content }} | 

      <div v-if="user_id === comment.author.id">
        <form @submit.prevent="updateComment">
          <input type="text" v-model.trim='inputComment'>
          <button type="submit">수정</button> |
          <button @click='deleteComment'>삭제</button>
        </form>
      </div>

    <button @click="likeComment" class= 'fun-btn'>
      <span v-if="!comment_isLike">좋아요</span>
      <span v-if="comment_isLike">좋아요 취소</span>
    </button>
    {{comment_like_users_count}}
    <div v-if="comment_like_users">
      <h6>좋아요 누른 사람</h6>
      <ul v-for="like_user in comment_like_users" :key="like_user.id">
          <img :src="`http://127.0.0.1:8000${like_user.profile_image}`" alt="프로필 이미지">
        <router-link :to="{name: 'ProfileView', params: { username : like_user.username}}">
          {{like_user.nickname}}
        </router-link>
      </ul>
    </div>
    


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
import axios from 'axios'
const DJANGO_URL='http://127.0.0.1:8000'

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
      created_at: this.comment.created_at,
      flagShowButtonUD : true,
      inputComment: this.comment.content,
    }
  },
  computed: {
    comment_isLike() {
      return this.comment_like_users.some(user => { return user.id === this.user_id })
    },
  },
  methods: {

    updateComment() {
      if ( !this.inputComment ) {
        alert('내용을 입력해주세요 :<')
        this.inputComment = this.comment.content
      }else {
        const payload = {
          comment_id : this.comment.id,
          content : this.inputComment
        }
        this.$store.dispatch('updateComment', payload)
      }
    },

    deleteComment() {            
      this.$store.dispatch('deleteComment', this.comment)
    },

    likeComment() {
      axios({
        method: 'put',
        url: `${DJANGO_URL}/api/v2/movies/like/${this.comment.id}/`,
        headers: { Authorization : `Token ${this.$store.state.token}` },
      })
      .then(res => {
        console.log(res)
        
        const data = res.data
        this.comment_like_users_count = data.count
        this.comment_like_users = data.like_users
      })
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
}
</script>

<style>

</style>