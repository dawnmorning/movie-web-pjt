<template>

  <div class='bodyWrap' v-if="review" >
    <!-- {{review}} -->
    <div class="card-body border border-secondary" style='border-radius:0.3cm'>
      <div class='needinLine' v-if="profileImage" style="height:50%; text-aling:center">
        <a class='jua' style='none; color:; font-size:smaller; height:10%; margin:0px;' :href="`http://localhost:8080/profile/${review.author.username}`"></a>
        <div class="splide-card m-1" :style="`  border-radius: 40%; background-image: url(${profileImage});`"></div>
        <p class="card-text" style='font-size:16px; margin-top:10px;'>{{review.author.nickname}}</p>  
        <div>
          <div v-show="isAuthor">
            <button 
            @click="goEditReview"
             class='jua btn-open-popup' style='font-size:small; margin-left:370px;
              margin-top:15px; border-radius:0.3cm; border-color: rgba(0,0,0,0);r'>✏️
            </button>
          </div>
        </div>
      </div>
    </div>
      
      <img class='reviewimg ' :src='`https://image.tmdb.org/t/p/w500/${review.movie.poster_path}`'>
      <hr>       
      <h5 class="card-title" style='text-align:center;'>영화 : {{review.movie.title}}</h5>
      
      <hr>
      <div class="card-body">
        <h5 class="card-title mb-2">리뷰 : {{review.title}}</h5>
        <p class="card-subtitle mb-2">{{review.content}}</p>
        <h5 class="card-text mb-2 text-muted">작성일 : {{review.updated_at.split('T', 1)[0]}}</h5>
        <star-rating id="setstar" :star-size="15" v-model="rating" :border-width="5" border-color="#d8d8d8" read-only=true
          :rounded-corners="true" 
          :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]">
        </star-rating>
        <button @click="likeReview" class='fun-btn' style='width:30px;'>
          <span v-if="!review_isLike"><i class="fa-regular fa-heart"></i></span>
          <span v-if="review_isLike"><i class="fa-solid fa-heart"></i></span>
        </button>
        {{review_like_users_count}}
        <div v-if="review_like_users">
          <h6>좋아요 누른 사람</h6>
          <ul v-for="review_like_user in review_like_users" :key="review_like_user.id" style='padding:0;'>
              <img :src="`http://127.0.0.1:8000${review_like_user.profile_image}`" alt="프로필 이미지" style='width:10%;'>
              <router-link :to="{name: 'ProfileView', params: { username : review_like_user.username}}" style='text-decoration-line: none;'>
                  {{review_like_user.nickname}}
              </router-link>
          </ul>
        </div>
      </div>
      
        <!-- 댓글 -->
        
        <hr style='margin:0px;'>
        <!-- <h5>댓글 입력</h5> -->
      <form class='commentstyle'>       
        <input type="text"
        v-model="inputData"
        @keyup.enter="createComment"
        placeholder="댓글 달기"
        style= 'width:100%;' 
        >
        <div @click="createComment" class='buttonstyle'>입력</div>
        
        <!-- 모달 -->
        <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal" style='font-size:15px; width:70px;'>
          댓글보기
        </button>
        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">댓글목록</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body" style='right:350px;' v-if="comments">
                <div v-for="comment in comments" :key="comment.id">
                  <CommentListItem
                  :comment=comment
                  />
                </div>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
</template>
<script>
import CommentListItem from '@/components/CommentListItem'
import axios from 'axios'
import StarRating from 'vue-star-rating'

// const IMG_URL = "https://image.tmdb.org/t/p/w500"
// console.log(review.author.profile)
const DJANGO_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewListItem',
  props:{
      review:Object,
  },
  components: {
      CommentListItem,
      StarRating,
  },
  data() {
      return {
        inputData: null,
        // is_open : false,
        review_like_users: this.review.like_users, 
        review_like_users_count: this.review.cnt_like_users,
        rating: this.review.rating,
      }
  },
  computed:{
    user_id() { return this.$store.state.user_id },
    comments() { return this.review.comments },
    review_isLike() { return this.review_like_users.some(user => { return user.id === this.user_id })},
    profileImage() { return DJANGO_URL+this.review.author.profile_image },
    isAuthor() { return this.user_id === this.review.author.id}

  },

  methods: {
    goEditReview() {
      console.log(this.review)
      
      this.$router.push({name: 'EditReview', params: { review_id: this.review.id}})

    },
    createComment() {
        const payload = {
            review_id: this.review.id,
            comment: this.inputData,
        }
        this.$store.dispatch('createComment', payload)
        this.inputData = null
    },
    // isopen(){
    //   this.is_open= true
    // },

    // isclose(){
    //   this.is_open= false
    // },
    getReview() {
      axios({
        method: 'get',
        url:`${DJANGO_URL}/api/v3/review/${this.review_id}/detail/`,
        headers:{
          Authorization : `Token ${this.$store.state.token}`,
        },
      })
      .then(res => {
        this.review_like_users = res.data.like_users,
        this.review_like_users_count = res.data.cnt_like_users,
        this.review_isLike =  res.data.like_users.some(like_user => { return like_user.id === this.user_id })        
      })
      .catch(err => { console.log(err)})
      
    },
    
    likeReview() {
      axios({
        method: "put",
        url: `${DJANGO_URL}/api/v3/review/like/${this.review.id}/`,
        headers: { Authorization: `Token ${this.$store.state.token}` }
      })
      .then(res => {
        const data = res.data
        this.review_like_users = data.like_users,
        this.review_like_users_count = data.count,
        this.review_isLike =  data.is_like
        
      })
    },
  },
}
</script>

<style>
.clickcursor{
  cursor: pointer;
  text-align: center;
 
}
.bodyWrap{
    /* width:500px; */
    /* height: 945px; */
    display: block;
    font-family: 'Jua-Regular';
    /* margin-top: 50px auto;
    margin-bottom : 100px auto; */
}
.reviewimg{
  width:100%; height: 100%;
  /* height:600px; */
  /* width: 500px; */
  /* object-fit: cover; */
}
div .card-body{
  padding:0px;
  /* 이건 100%가 맞음 */
  /* height: 100%; */
}

.buttonstyle{
  cursor: pointer;
  width: 35px;
  height: 20px;
  /* font-size:10px; */
  display: inline;
  position: relative;
  top: 20px;
  text-align: center;
  /* right: 30px; */

}
.commentstyle{
  margin-top: 0px;
  /* position: sticky; */
  
  text-align: right;
  display: flex;
  overflow: auto;
}
/* 모달 */
.userImage{
  width:10%;
}
.needinLine{
  display: flex;
  flex-wrap: nowrap;
}
.splide-card {
  height: 40px;
  width: 30px;
  background-size: cover;
  background-position: center center;
}
</style>