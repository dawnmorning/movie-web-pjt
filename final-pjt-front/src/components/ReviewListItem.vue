<template>

  <div class='bodyWrap'>
    <!-- {{review.comments}} -->
    <div class="card-body">
      <div class='needinLine'>
        <img :src=profileImage alt="" class='userImage'>
        <p class="card-text" style='font-size:16px; margin-top:5px;'>{{review.author.nickname}}</p>

      </div>
        <img class='reviewimg' :src='`https://image.tmdb.org/t/p/w500/${review.movie.poster_path}`'>
        <hr>       
        <h5 class="card-title" style='text-align: center;'>영화 : {{review.movie.title}}</h5>
    
        <hr>
        <div class="card-body">
          <h5 class="card-title">리뷰 : {{review.title}}</h5>
          <h5 class="card-subtitle mb-2 text-muted">{{review.updated_at}}</h5>
          <h5 class="card-subtitle mb-2 text-muted">별점 : {{review.rating}}</h5>
          <p class="card-text">{{review.content}}</p>
        </div>
        
        <!-- 댓글 -->
        <CommentList
        :comments=review.comments
        />

        <hr style='margin:0px;'>
        <!-- <h5>댓글 입력</h5> -->
        <form class='commentstyle'>
          <input type="text"
          v-model="inputData"
          @keyup.enter="createComment"
          placeholder="댓글 달기"
          style= 'width: 100%;' 
          >
          <div
          @click="createComment"
          class='buttonstyle'
          >입력</div>
          <!-- 모달 -->
          <div @click='isopen' class='clickcursor'>댓글모두 보기</div>
          <div class='black-bg' v-if='is_open'>
            <div class='white-bg'>
              <h4>댓글 목록</h4>
              <p>댓글 내용</p>
            </div>
              <button @click= 'isclose'>닫기</button>
          </div>
        </form>
    </div>
  </div>
</template>
<script>
import CommentList from '@/components/CommentList'
// const IMG_URL = "https://image.tmdb.org/t/p/w500"
// console.log(review.author.profile)
const DJANGO_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ReviewListItem',
    data() {
        return {
            inputData: null,
            is_open : false,
        }
    },
    components: {
        CommentList,
    },
    props:{
        review:Object,
    },
    // computed: {
    //     comments() {
    //         return this.review.comments
    //     }
    // },
    methods: {
      createComment() {
          const payload = {
              review_id: this.review.id,
              comment: this.inputData,
          }
          this.$store.dispatch('createComment', payload)
          this.inputData = null

      },
      isopen(){
        this.is_open= true
        console.log(this.is_open)
      },
      isclose(){
        this.is_open= false
      }
    },
    created() {
        // console.log(this.review.comments)
        // console.log(this.review.movie)
    },
    computed:{
      profileImage(){
        return DJANGO_URL+this.$store.state.profile_image
      }
    }
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
  /* position: relative; */
  top: 15px;
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
.black-bg{
  box-sizing: border-box;
  width : auto; height: auto;
  background:  rgba(0,0,0,0.5);
  position: fixed; padding: 20px;
  position: absolute;
  z-index: 10;
  bottom: 150px;
} 
.white-bg{
  width: auto; background: white;
  height: auto; 
  border-radius: 8px;
  padding: 20px;
   position: absolute;
  z-index: 10;
  text-align: center;
  justify-content: center;
  bottom: 10px;   
}
.userImage{
  width:10%;
}
.needinLine{
  display: flex
}
</style>