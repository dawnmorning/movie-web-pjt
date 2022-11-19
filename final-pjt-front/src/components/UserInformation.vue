<template>
  <!-- <div style="overflow: scroll;"> -->
    
    <div style='margin:100px;'>
      <!-- profile -->
      <div class="continer">
        
          <div class="profile">
              <div class="profile_img">
                  <img :src="profileImage" alt="프로필 이미지">
              </div>
              <div class="info">
                  <div class="area_text">
                      <div v-if='information.nickname'>
                          <h2 class="user_id">{{ information.nickname }}</h2>
                      </div>
                      <div v-if='!information.nickname'>
                          <h2 class="user_id">{{ username }}</h2>
                      </div>
                      <a href="" class="profile_edit">프로필 수정</a>
                      <button type="button" class="setting_btn">
                          <i class="fas fa-cog"></i>
                      </button>
                  </div>
                  <div class="area_text">
                      <div class="tit_desc">
                          <span class="title">게시물</span>
                          <span class="sub_title">7</span>
                      </div>
                      <div class="tit_desc">
                          <span class="title">팔로워</span>
                          <span class="sub_title">10</span>
                      </div>
                      <div class="tit_desc">
                          <span class="title">팔로우</span>
                          <span class="sub_title">15</span>
                      </div>
                  </div>
                  <div class="area_text profile_info">
                      <h3 class="info_title">안녕하세요.</h3>
                      <p class="info_sub">네 지나가세요~</p>
                  </div>
              </div>
          </div>
          <!-- p// rofile -->
          <!-- contents -->
                      <div class="contents">
                          <div class="tab_box">
                              <ul class="tab_list">
                                  <li class="active">
                                      <a href="">
                                          <i class="fas fa-list"></i>
                                          <span>게시물</span>
                                      </a>
                                  </li>
                                  <li>
                                      <a href="">
                                          <i class="fas fa-tv"></i>
                                          <span>IGTV</span>
                                      </a>
                                  </li>
                                  <li>
                                      <a href="">
                                          <i class="fas fa-bookmark"></i>
                                          <span>저장됨</span>
                                      </a>
                                  </li>
                                  <li>
                                      <a href="">
                                          <i class="fas fa-user-tag"></i>
                                          <span>태그됨</span>
                                      </a>
                                  </li>
                              </ul>
                          </div>
                          <div class="boards">
                              <ul class="board_list ">
                                  <li>
                                      <a href="">
                                          <div class="board_img">
                                              <img src="" alt="이미지">
                                          </div>
                                      </a>
                                  </li>
                                  <li>
                                      <a href="">
                                          <div class="board_img">
                                              <img src="" alt="이미지">
                                          </div>
                                      </a>
                                  </li>
                                  <li>
                                      <a href="">
                                          <div class="board_img">
                                              <img src="" alt="이미지">
                                          </div>
                                      </a>
                                  </li>
                                  <li>
                                      <a href="">
                                          <div class="board_img">
                                              <img src="" alt="이미지">
                                          </div>
                                      </a>
                                  </li>
                                  <li>
                                      <a href="">
                                          <div class="board_img">
                                              <img src="" alt="이미지">
                                          </div>
                                      </a>
                                  </li>
                                  <li>
                                      <a href="">
                                          <div class="board_img">
                                              <img src="" alt="이미지">
                                          </div>
                                      </a>
                                  </li>
                                  <li>
                                      <a href="">
                                          <div class="board_img">
                                              <img src="" alt="이미지">
                                          </div>
                                      </a>
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

const DJANGO_URL='http://127.0.0.1:8000'

export default {
    name : 'UserInformation',
    data(){
        return{
            information : '',
            profileImage : '',
        }
    },
    computed: {
        username() {
            return this.$store.state.username
        }
    },
    created(){
        axios({
            method:'get',
            url: `${DJANGO_URL}/api/v1/profile/${this.username}/`,
            headers:{
                Authorization : `Token ${this.$store.state.token}`,
            }
            // withCredentials: true,
        })
            .then(res =>{
                // console.log(res)
                this.information = res.data
                this.profileImage = `${DJANGO_URL}` + res.data.profile_image
                // console.log(this.information)
                console.log(res)
            })
    },
    methods:{
        goModify(){
            this.$router.push({name: 'EditProfile', params: {username: this.username}})
        }
    }
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
</style>