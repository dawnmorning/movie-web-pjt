<template>
  <div class="container" v-if="reviews">
    <div>나는야 홈런왕</div>
    <div class='left_body' v-for="review in reviews" :key="review.id">
        <ReviewListItem
        :review=review
        />
    </div>
    <div class='right_body'>
      <div class=profile_box>
        <img class='profile_img' :src=profileImage alt="">
        <div>{{ this.$store.state.username }}</div>
        <div class='nickname'>{{ this.$store.state.nickname }}</div>
        <div></div>
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
      }
    },
    components: {
        ReviewListItem,
    },
    computed:{
      reviews(){
        return this.$store.state.reviews
      },
      profileImage(){
        return DJANGO_URL+this.$store.state.profile_image
      }
    },
    created() {
      this.$store.dispatch('getReviews')
    },
    methods:{
    }
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
.nickname{
  color: blue;
  font-weight: 500;
  opacity:0.3;
  margin-top: 5px;
}
</style>