<template>
  <div class="container" v-if="reviews" style='margin-top:30px;'>
    <!-- 팔로워 목록 -->
    <div v-if="myFollowings" style='margin-top:50px;'>
      <div v-for="myFollowing in myFollowings" :key="myFollowing.id">
        <div class='profile_box' style='width:100px;'>
          <a class='jua' style='text-decoration: none; color:; font-size:smaller ' :href="`http://localhost:8080/profile/${myFollowing.username}`">
          <img class='profile_img' :src="`http://127.0.0.1:8000${myFollowing.profile_image}`" alt="" style='display:inline;'>
          <p>{{myFollowing.nickname}}</p>
          </a>
        </div>
      </div>
    </div>

    <!-- 리뷰 자리 -->
    <div class='left_body' >
      <div v-for="review in reviews" :key="review.id" style='margin-top:20px;'>
        <ReviewListItem
        :review=review
        />
      </div>
    </div>
    
    <!-- 프로필 자리 -->
    <div class='right_body' v-if="profileImage">
      <div class='profile_box'>
        <a class='jua' style='text-decoration: none; color:; font-size:smaller ' :href="`http://localhost:8080/profile/${username}`">
          <img class='profile_img' :src=profileImage alt="">
          <div v-if="username">{{ username }}</div>
          <div class='nickname'>{{ this.$store.state.nickname }}</div>
        </a>
      </div>
    </div>
  </div>
</template>

<script>

const DJANGO_URL = 'http://127.0.0.1:8000'
import ReviewListItem from '@/components/ReviewListItem'

export default {
  name:'ReviewList',
  data(){
    return{
      username: this.$store.state.username,
    }
  },
  components: {
      ReviewListItem,
  },
  computed:{
   myFollowings() {
      return this.$store.state.followings
    },
   following_ids() {
      const following_ids = this.$store.state.followings.map(following => { return following.id })
      return following_ids
    },

    reviews(){
      const following_reviews = this.$store.state.reviews.filter( review => {
        return this.following_ids.includes(review.author.id) || this.$store.state.user_id ===  review.author.id
      } )
      return following_reviews
    },

    profileImage(){
      return DJANGO_URL+this.$store.state.profile_image
    },


  },

  created() {
    this.$store.dispatch('getReviews')
    this.$store.dispatch('getFollowings')
  },

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel&display=swap');
.container{
  display:block;
  margin-top: 50px;
  font-family: 'Cinzel', serif;
  width : 822px;
  justify-content: center;
  /* font-family: 'Dongle-Light'; */
  /* flex-direction: column; */
}

.main_body {
  display: flex;
  justify-content: center;
  padding-top: 50px;
}

.left_body {
  /* background-color: skyblue; */
  position: relative;
  margin: 0px 400px 0 ;
  right: 20%;
  /* width: 500px; */
  /* height: 945px; */
  display: flex;
  flex-direction: column;
  object-fit: contain;
  margin-top: 50px;
  /* left: 100px; */

  /* height:2000px; */
  /* margin-bottom: 400px; */



  /* position: relative;
  
  width: 600px;
  height: 100%; */
}

.right_body {
  /* background-color: yellow;  */
  position : absolute;
  top : 17%;
  right: 500px; 
  width:320px; 
  height:1000px; 
  /* position: sticky; */

}
  /* position: fixed;
  right: 600px; */
.feed_box {
  background-color:white;
  width: 480px;
  margin:10px;
  min-height:auto;
  clear: both;
}
.feed_img {
  width:100%;
  height:80%;
  object-fit: contain;
}

.feed_content {
  padding: 0px 10px;
}

.feed_like {
  padding:0px 10px;
}

.feed_reply {
  padding:0px 10px;
  display:flex;
  flex-direction:column;
}

.feed_txt {
  font-size:14px;
}

.feed_icon {
  padding:5px 5px 0px 5px;
  display:flex;
  justify-content:space-between;
}
span{
  padding-right:5px;
}
.feed_name {
  padding: 10px;
  display:flex;
  align-items:center;
}
.feed_name_txt {
  font-size:14px;
  padding:0px 10px;
  font-weight: bold;
}
.profile_box {
  width: 319px;
  height: 66px;
  /* border-radius: 20%; */
  /* overflow:; */
}
.profile_img {
  width:50%;
  height:100%;
  object-fit: cover;
  object-fit:cover;
}
a {
  text-decoration: none;
}
</style>