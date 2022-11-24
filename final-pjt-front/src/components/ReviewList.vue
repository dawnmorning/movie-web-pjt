<template>
  <div class="container" v-if="reviews" style='margin-top:-110px;'>  
    <div class='left_body float-md-start'  >
      <!-- 팔로워 목록 -->
      <div class="d-flex flex-row card-body border border-secondary align-items-bottom"  v-if="myFollowings" style='border-radius:0.3cm; margin-top:150px; width:494px; height:119px; position:relative;'>
        <carousel class="slide" style="overflow:auto" :per-page="4" :navigate-to="someLocalProperty" :mouse-drag="true">
          <slide style='text-align:center; margin-left:-20px;' v-for="myFollowing in myFollowings" :key="myFollowing.id" class='slide__item '>
            <div class='profile_box' style='width:100px; position:relative; top:35px; height:119px;'>
              <a class='jua' style='text-decoration: none; font-size:smaller ' :href="`http://localhost:8080/profile/${myFollowing.username}`">
                <div><img  class='profile_img' :src="`http://127.0.0.1:8000${myFollowing.profile_image}`" alt="" style='display:inline; width:50px; height:50px;'></div>
                <p>{{myFollowing.nickname}}</p>
              </a>
            </div>
          </slide>
        </carousel>
      </div>
      <!-- 리뷰 자리 -->
      <div v-for="review in reviews" :key="review.id" style='margin-top:20px;'>
        <ReviewListItem
        :review=review
        />
      </div>
    </div>
    
    <!-- 프로필 자리 -->
      <div class='right_body float-md-start' v-if="profileImage">
        <div>
          <div class='jua' style='margin-top:0px; font-size:15px;'>내 프로필</div>
        </div>
          <div class='profile_box' style='position:relaitve; top:100px;'>
                <a text=black; class='jua' style='text-decoration: none; text:black; font-size:smaller position:relaitve; top:50px; width:10px; height:10px; font-size:20px;' :href="`http://localhost:8080/profile/${username}`">
                  <div style='background-color: #f5f5f5;'> <img style='float:left; position:relative; top:-10px; width:80px; ' class='profile_img' :src=profileImage alt=""></div>
                </a>
                <div style='text-align:left; width:300px; height:100%; '>
                  <a v-if="username" class='jua' style='text-decoration:none; font-size:20px;' :href="`http://localhost:8080/profile/${username}`">
                    {{ username }}
                  </a>  <br>
                  <a class='jua' style='text-decoration: none; font-size:20px;' :href="`http://localhost:8080/profile/${username}`">
                      {{ this.$store.state.nickname }}
                  </a>

                </div>
            </div>
      </div>
  </div>
</template>

<script>

const DJANGO_URL = 'http://127.0.0.1:8000'
import ReviewListItem from '@/components/ReviewListItem'
import { Carousel, Slide } from 'vue-carousel';

export default {
  name:'ReviewList',
  data(){
    return{
      username: this.$store.state.username,
    }
  },
  components: {
      ReviewListItem,
      Carousel,
      Slide,
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
  position : absolute;
  top : 15%;
  right: 500px; 
  width:320px; 
  height:100%; 
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
   width: 150px;
    height: 150px; 
    border-radius: 70%;
    /* overflow: hidden; */
}
.profile_img {
 width: 100%;
    height: 100%;
    object-fit: cover;
 background-color: #f5f5f5;
 border-radius: 70cm;
} 
a {
  text-decoration: none;
}
html{
  background-color: #f5f5f5;
}
.VueCarousel-pagination {
  background-color:rgba(0,0,0,0);
  display: none;
}
</style>