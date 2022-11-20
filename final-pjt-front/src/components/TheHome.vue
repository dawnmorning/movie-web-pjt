<template>
  <div>
    <!-- 로그인 시 보일 화면 -->
    <div v-if='isLogin'>
<<<<<<< HEAD
      <div class='jua animate__animated animate__backInUp delay-4s'>
        <div class=''>안녕하세요, {{ username }}</div> 
=======
      <div class='mx-auto jua animate__animated animate__backInUp delay-4s'>
        <div class=''>안녕하세요, {{ nickname }} 님</div> 
>>>>>>> 5f366e8cda8e2be596368a12807df0fcd966c854
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
    name: 'TheHome',
    components:{
      LogIn
    },
    data(){
      return{
      }
    },
    computed:{
      nickname() {
        return this.$store.state.nickname
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