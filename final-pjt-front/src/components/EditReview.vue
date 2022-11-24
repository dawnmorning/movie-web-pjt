<template>
  <div v-if="review">
<br>
<br>
<br>
    <div>
      {{ review }}
    </div>
    <div class='jua juaDetail' :style="`background-image: url(https://image.tmdb.org/t/p/w500/${movie.poster_path})`" ></div>
    <div class='reviewbody' style='margin-top: 100px; color:white;'>

			<div id="box" class='postfont animate__animated animate__fadeIn animate-delay-2s'>
        <div style='width"100%; text-align:center;'>
        <img class='img-fluid' :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="" style='position:relative; width"100%; border-radius: 0.5cm; height:400px; '>
        </div>
				<h1 class="heading" style='font-weight:600;'>{{movie.title}}</h1>
				<div class="data">
					<span class="average" style='color:white;'>평점 {{movie.vote_average}}</span>
				</div>
				<p class="texts" style='font-size:17px;'>
					{{movie.overview}}
				</p>
				<div style='text-align: center;'>
					<button @click='showModal' class='jua btn-open-popup' style='font-size:15px; margin-top: -30px; width:80px; border-radius:0.3cm;' 
					data-bs-toggle="modal" data-bs-target="#staticBackdrop">리뷰쓰기
          </button>
					<button @click='goBack' class='jua btn-open-popup' style='font-size:15px; margin-top: -30px; width:80px; border-radius:0.3cm;' 
					>뒤로가기
					</button>
				</div>
      </div>
      
      <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered jua">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="text-align-center modal-title fs-5" id="staticBackdropLabel">리뷰 작성</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" style='font-size:20px;'></button>
            </div>
            <div class="modal-body jua" style='margin-top:10px;'>
              <div class='reviewModal' v-if='is_show' style='text-align:center; margin-top:10px; '>
              <div class="ReviewInlineblock" style= 'width: 400px;'>
                  <input style=' width:400px;' type="text" id='username' v-model='title' placeholder="제목" class='id'>
              </div>
              <div class="ReviewInlineblock">
                  <input size='44' style=' height:100px; flex-wrap:wrap' type="text" id='content'  v-model='content' placeholder="내용" class='content'>      
              </div>
              <div class="ReviewInlineblock">
                <star-rating id=setstar :star-size="30" v-model="rating" :border-width="5" border-color="#d8d8d8" 
                :rounded-corners="true" 
                :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]">
                </star-rating>
              </div>
              </div>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>

                <button type="button" class="btn btn-primary" data-bs-dismiss="modal">작성하기</button>
              </div>
          </div>
        </div>
      </div>
    </div>

     <!-- "id": 26,
       "movie": { "id": 2245, "like_users": [], "cnt_like_users": 0, "movie_id": 661374, "title": "나이브스 아웃: 글래스 어니언", "original_title": "Glass Onion: A Knives Out Mystery", "overview": "가장 아끼는 친구들을 본인의 사유지인 그리스의 섬으로 초대한 IT계의 억만장자 마일스 브론(에드워드 노튼). 하지만 머지않아 이곳이 마냥 낙원이 아니라는 사실이 드러난다.", "poster_path": "/lrgmo1qluO9c2qdBduiu412fRDS.jpg", "backdrop_path": "/1gKurtZWrqsXB7mSYWY0W4CpUjl.jpg", "release_date": "2022-11-23", "popularity": 32.512, "vote_average": 0, "vote_count": 0, "adult": false }, 
       "author": { "id": 1, "username": "lwi995", "email": "lwi995@naver.com", "nickname": "이원일", "profile_image": "/media/profile/2022/11/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.jpg", "grade": 0, "
       followings": [ { "id": 2, "username": "admin", "nickname": "창조주", "profile_image": "/media/default5.jpg", "grade": 0, "followings": [ 1 ] },  { "id": 4, "username": "rlawhdgur", "nickname": "김종혁", "profile_image": "/media/default7.jpg", "grade": 0, "followings": [] }, { "id": 5, "username": "rnjsdbwls", "nickname": "권유진", "profile_image": "/media/default7.jpg", "grade": 0, "followings": [] }, { "id": 6, "username": "tlsalscjf", "nickname": "신민철", "profile_image": "/media/default7.jpg", "grade": 0, "followings": [] }, { "id": 8, "username": "dldnjsdlf", "nickname": "이원일2", "profile_image": "/media/default1.jpg", "grade": 0, "followings": [] }, { "id": 9, "username": "kakao", "nickname": "카카오", "profile_image": "/media/default7.jpg", "grade": 0, "followings": [] }, { "id": 12, "username": "eeeeee", "nickname": "qdlfnasdio", "profile_image": "/media/default7.jpg", "grade": 0, "followings": [] }, { "id": 14, "username": "디버깅", "nickname": "디버깅", "profile_image": "/media/default7.jpg", "grade": 0, "followings": [] }, { "id": 16, "username": "gkwlsdn", "nickname": "하진우", "profile_image": "/media/default2.jpg", "grade": 0, "followings": [] }, { "id": 17, "username": "test11", "nickname": "한국", "profile_image": "/media/default3.jpg", "grade": 0, "followings": [] } ], 
       "followers": [ { "id": 2, "username": "admin", "nickname": "창조주", "profile_image": "/media/default5.jpg", "grade": 0, "followings": [ 1 ] } ], 
       "cnt_followings": 10, "cnt_followers": 1 }, 
       "like_users": [], "cnt_like_users": 0, "comments": [],
        "cnt_comments": 0, "title": "test", "content": "test", 
        "rating": 5, "created_at": "2022-11-24T05:00:02.424377Z",
         "updated_at": "2022-11-24T05:00:02.424377Z" } -->
 
  </div>
  </template>

<script>
import StarRating from 'vue-star-rating'

export default {
  name: "EditReview",
  components:{
    StarRating
  },
  data() {
    return {
      // review: this.$store.state.review_detail,
      title:null,
      content:null,
      rating:4,
      is_show : true,
    }
  },
  computed: {
    review() { return this.$store.state.review_detail },
    movie() {return this.review.movie },
  },
  methods: {
    showModal(){
      this.is_show = true
    },
    goBack() {
      this.$router.go(-1)
    },

  },
  created() {
    this.$store.dispatch('getReviewDetail', this.$route.params.review_id)
  }

}
</script>

<style>

</style>