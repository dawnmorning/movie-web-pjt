<template>
  <div>
    <!-- 로그인 시 보일 화면 -->
    <div v-if='isLogin'>
      <nav class="sticky-top navbar navbar-expand-lg navbar-light bg-light ">
        <div class="container-fluid">
          <a class="navbar-brand fs-1" href="#">우리 프로젝트 명</a>
          <b-button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                  data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                  aria-expanded="false" aria-label="Toggle navigation">
            <input class="form-control" style="width: 200px" type="search" placeholder="Search" aria-label="Search">
          </b-button>
          <div class="justify-content-end collapse navbar-collapse " id="navbarSupportedContent">
            <form class="d-flex justify-content-center">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>

            <ul class="nav justify-content-end fs-6">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="http://localhost:8080/">홈</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/community">커뮤니티</a>
              </li>
              <li class="nav-item">
                <!-- <router-link class='nav-link' :to="`/profile/${this.$store.state.username}`">내 프로필</router-link> -->
                <a class='nav-link' :href="`/profile/${username}`">내 프로필</a>
              </li>
              <li class="nav-item">
                <a @click='noToken' class="nav-link" href="#">로그아웃</a>
              </li>
            </ul>
          </div>
        </div>
    </nav>


    















      <div class='mx-auto jua animate__animated animate__backInUp delay-4s'>
        <div class=''>안녕하세요, {{ username }}</div> 
        <div class='mt-5 ' >오늘 기분은 어때요?</div>
        <b-button @click='goRecommend' class='btn btn-info btn-lg'><span>영화를 고르러 가볼까요?</span> </b-button>
      </div>
        
        <!-- 라우터링크에 애니메이션 넣기 -->
        <!-- <router-link :to="{name: 'RecomView'}">영화를 추천해줄게요!</router-link>
        <b-nav>
          <router-link :to="{name: 'HomeView'}">홈</router-link> |
          <router-link :to="`/profile/${this.$route.params.username}`">내 프로필</router-link> |
        <b-button @click='noToken'>로그아웃</b-button>
        </b-nav> -->
    </div>
    <!-- 비로그인 시 보일 화면 -->
    <div v-if='!isLogin'>
      <LogIn/>
    </div>
    
  </div>
</template>

<script>
import LogIn from '@/components/LogIn'
export default {
    name: 'HomeView',
    components:{
      LogIn
    },
    data(){
      return{
      }
    },
    computed:{
      username() {
        return this.$store.state.username
      },
      isLogin(){
          return this.$store.getters.isLogin
      },
    },
    methods:{
      noToken(){
        this.$store.state.token = null
        this.$store.state.username = null
        this.$store.state.nickname = null
        this.$store.state.interested = null
        this.$store.state.profile_image = null
        localStorage.clear()
        this.$router.push({name: "HomeView"})
      },
      goRecommend(){
        this.$router.push({name: "RecomView"})
      }
  },
}
</script>

<style>
@font-face{
  font-family: 'Jua-Regular';
  src:url('/font/Jua-Regular.ttf')
}
.jua{
  font-family: 'Jua-Regular';
  font-size: 50px;
  margin-top: 200px;
  text-align: center;
} 

nav{
   position: fixed;
  top: 0;
  height: 70px;
  left: 0;
  right: 0;
}
/* 12 */



/* 애니메이션 */


</style>