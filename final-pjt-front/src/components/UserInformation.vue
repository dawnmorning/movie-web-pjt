<template>
  <!-- <div style="overflow: scroll;"> -->
    <div style='margin:100px;'>
      <!-- profile -->
        <div class="continer">
            <div class="profile" v-if='nickname'>
                <div class="profile_img">
                    <img :src="profileImage" alt="프로필 이미지">
                </div>
                <div class="info">
                    <div class="area_text">
                        <div >
                            <h2 class="user_id">{{ nickname }} 님</h2>
                        </div>
                        <button
                        v-if="isMyProfile"
                        @click='goModify'>프로필 수정</button>
                        <button
                        v-if="!isMyProfile"
                        @click='follower'>
                        <span v-if="!isFollowing">팔로우</span>
                        <span v-if="isFollowing">팔로우 취소</span>
                        </button>

                    </div>
                    <div class="area_text">
                        <div class="tit_desc">
                            <span class="title">게시물</span>
                            <span class="sub_title">7</span>
                        </div>
                        <div class="tit_desc">
                            <span class="title">팔로워</span>
                            <span class="sub_title">{{ cnt_followings }}</span>
                            <span>{{ followings }}</span>
                            </div>
                            <div class="tit_desc">
                                <span class="title">팔로우</span>
                                <span class="sub_title">{{ cnt_followers }}</span>
                                <span>{{ followers }}</span>
                        </div>
                    </div>
                    <!-- <div class="area_text profile_info">
                        <h3 class="info_title">안녕하세요.</h3>
                        <p class="info_sub">창조주 </p>
                    </div> -->
                </div>
            </div>
          <!-- profile -->
          <!-- contents -->
            <div class="contents" v-if="username">
                <div class="tab_box">
                    <ul class="tab_list">
                        <li class="active">
                            <a @click="getMyReviewList">
                                <i class="fas fa-list"></i>
                                <span>게시물</span>
                            </a>
                        </li>
                        <li>
                            <router-link :to="{name : '' }">
                                <i class="fas fa-tv"></i>
                                <span>컬랙션</span>
                            </router-link>
                        </li>
                    </ul>
                </div>
                
                <div class="boards">
                    <ul class="board_list " v-if="myReviews">
                        <li v-for="myReview in myReviews" :key="myReview.id">
                            <span @click="goReviewDetail(myReview)">
                                <img :src="`https://image.tmdb.org/t/p/w500/${myReview.movie.poster_path}`">
                                <p>좋아요 수 : {{ myReview.like_users.length }}</p>
                                <p>좋아요한 사람 : {{ myReview.like_users }}</p>
                            </span>
                            <!-- <MyReviewItem :myReview='myReview'/> -->
                        </li>
                    </ul>
                </div>
            </div>
            <!-- // contents -->
        </div>
    </div>
  <!-- </div> -->
    <!-- <nav> -->
        <!-- <p>Hello, {{ username }} </p> -->
        <!-- <div class='entireWrpap'>
          <div class='imgWrap'>
            <div class = 'profile_img'>
              <img :src="profileImage" alt="프로필 이미지">
            </div>
          </div>
          <div class='detail'>
            <div class='top'>
              <div>{{ username }}</div>
              <div>닉네임  {{ information.nickname }}</div>
            </div>  
          </div>  
          <ul class='middle'>
            <li>
              <div>관심장르  {{ information.interested }}</div>
            </li>
            <li>
              <div>등급  {{ information.grade }}</div>
            </li>
          </ul>
        </div> 
        <button @click='goModify'>프로필 수정</button>
    </nav> -->

</template>

<script>
import axios from 'axios'
// import MyReviewItem from './MyReviewItem.vue'
const DJANGO_URL='http://127.0.0.1:8000'

export default {
    name: "UserInfomation",
    data() {
        return {
            username: null,
            nickname: null,
            profileImage: null,
            email: null,
            grade: null,
            cnt_followers: null,
            cnt_followings: null,
            followers: null,
            followings: null,
            isFollowing: null,
            myReviews: null,
        };
    },
    computed: {
        isMyProfile() {
            return this.$route.params.username === this.$store.state.username;
        }
    },
    methods: {
        goModify() {
            this.$router.push({ name: "EditProfileView", params: { username: this.username, nickname: this.nickname, profile_img: this.profileImage, email: this.email } });
        },
        getProfile() {
            axios({
                method: "get",
                url: `${DJANGO_URL}/api/v1/${this.$route.params.username}/`,
                headers: { Authorization: `Token ${this.$store.state.token}` }
            })
                .then(res => {
                const userInfo = res.data;
                const user_id = this.$store.state.user_id;
                this.username = userInfo.username;
                this.nickname = userInfo.nickname,
                this.profileImage = DJANGO_URL + userInfo.profile_image,
                this.email = userInfo.email,
                this.grade = userInfo.grade,
                this.cnt_followers = userInfo.cnt_followers;
                this.cnt_followings = userInfo.cnt_followings;
                this.followers = userInfo.followers;
                this.followings = userInfo.followings;
                this.isFollowing = userInfo.followers.some(follower => { return follower.id === user_id; });
            });
        },
        follower() {
            axios({
                method: "put",
                url: `${DJANGO_URL}/api/v1/follow/${this.username}/`,
                headers: { Authorization: `Token ${this.$store.state.token}` }
            })
                .then((res) => {
                const data = res.data;
                this.isFollowing = data.is_following;
                this.followers = data.followers;
                this.followings = data.followings;
                this.cnt_followers = data.cnt_followers;
                this.cnt_followings = data.cnt_followings;
            }).catch(() => { });
        },
        getMyReviewList() {
            const username = this.$route.params.username;
            axios({
                method: "get",
                url: `${DJANGO_URL}/api/v3/reviews/${username}/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`,
                },
            })
                .then((res) => {
                this.myReviews = res.data;
            })
                .catch(err => { console.log(err); });
        },
        goReviewDetail(myReview) {
            this.$router.push({name: 'ReviewDetail' , params : {review_id: myReview.id}})
        }
    },
    created() {
        this.getProfile(),
            this.getMyReviewList();
    },
    // components: { MyReviewItem }
}
</script>

<style>
.main {
    position: relative;
    top: 55px;
    background: #f8f9fa;
}
.main .container {
    max-width: 1040px;
    margin: 0 auto;
    padding-top: 30px;
}

/* profile */
.profile {
    display: flex;
    align-items: center;
    margin-bottom: 35px;
}
.profile .profile_img {
    margin: 0 70px;
}
.profile .profile_img img {
    width: 150px;
    height: 150px;
    border-radius: 50%;
}
.profile .info {
   width: 100%;
   margin: 0 30px;
}
.profile .info .area_text {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    margin-bottom: 10px;
    line-height: 1.7;
}
.profile .info .area_text .user_id {
    font-size: 30px;
    margin-right: 20px;
}
.profile .info .area_text .profile_edit {
    margin-right: 20px;
    padding: 7px 10px;
    border: 1px solid  #dbdbdb;
    border-radius: 5px;
    color: #000;;
    font-size: 15px;
}
.profile .info .area_text .setting_btn {
    border: none;
    background: none;
    outline: none;
    cursor: pointer;;
}
.profile .info .area_text .setting_btn i {
    font-size: 25px;
}
.profile .info .area_text .tit_desc {
    margin-right: 20px;
}
.profile .info .area_text .tit_desc .title {
    padding-right: 5px;
}
.profile .info .area_text .tit_desc .sub_title {
    font-weight: bold;
}
.profile .info .area_text.profile_info {
    display: block;
}
.profile .info .area_text.profile_info .info_title {
    font-weight: bold;
}
.profile .info .area_text.profile_info .info_sub {

}
/* // profile */
/* contents */
.contents {
    border-top: 1px solid #dbdbdb;
}
.contents .tab_box {
    
}
.contents .tab_box .tab_list {
    display: flex;
    justify-content: center;
}
.contents .tab_box .tab_list li {
    display: flex;
    align-items: center;
    position: relative;
    margin: 0 20px;
    font-size: 15px;
    line-height: 1.4;
}
.contents .tab_box .tab_list li.active::after {
    display: block;
    content: "";
    position: absolute;
    top: -1px;
    left: 0;
    border-top: 1px solid #000;
    width: 100%;
    height: 100%;
}
.contents .tab_box .tab_list li a {
    display: block;
    padding: 20px 0;
    cursor: pointer;
    color: #868e96;
}
.contents .tab_box .tab_list li.active a {
    display: block;
    color: #000;
}
.contents .tab_box .tab_list li i {
    padding-right: 5px;
}

.contents .boards {
    margin-top: 20px;
}
.contents .boards .board_list {
    display: flex;
    flex-wrap: wrap;
}
.contents .boards .board_list li {
    width: 293px;
    height: 293px;
    margin: 0 26px 20px;
}
.contents .boards .board_list li a {
    display: block;
    height: 100%;
    width: 100%;
}
.contents .boards .board_list li a .board_img {
    position: relative;
    width: 100%;
    height: 100%;
}
.contents .boards .board_list li a .board_img img {
    width: 100%;
    height: 100%;
}
/* //contents */
/* footer */
.footer {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 30px;
}
.footer span {
    font-size: 18px;
    line-height: 1.4;
}
.black-tg{
  width:100%;
  height:100%;
  background: rgba(0,0,0,0.6);
  position: fixed;
}
.white-bg{
  width:90%;
  margin: 80px auto;
  background: white;
  padding: 20px 0;
}
.close{
  cursor: pointer;
  border: none;
  background: #6667AB;
  color: white;
  font-weight: bold;
  border-radius: 5px;
  padding: 5px 15px;
}
.close:hover{
  color: white;
  font-weight: bold;
  transform: scale(1.1);
  transition: all 0.5s;
}
</style>