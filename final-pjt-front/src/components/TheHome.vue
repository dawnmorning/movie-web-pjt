<template>
  <div style='position:realted'>
    <!-- 로그인 시 보일 화면 -->
    <div v-if='isLogin' >
      <div class='jua animate__animated animate__backInUp delay-4s' style='color:black; margin-top:250px;'>
        <div class=''>안녕하세요, {{ nickname }} 님</div> 
        <div class='mt-5 ' >오늘 기분은 어때요?</div>
        <b-button @click='goRecommend' class='btn btn-info btn-lg'><span>영화를 고르러 가볼까요?</span> </b-button>
      </div>
      <div>
      <div class="today jua " style='display:inline; position:related; right:1200px;'>
          <div class='visitor animate__animated animate__heartBeat animate__repeat-3 delay-4s'>
              <p>오늘 방문자 수</p>
              <number class="number" :from="0" :to="1125" :duration="6"/>
          </div>
      </div>
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
.today {
    margin: 50px auto;
    text-align: center;
}

.today p {
    font-size: 50px;
    line-height: 1;
}

.visitor {
    margin: 30px 0 0 0;
    padding: 30px;
    font-size: 40px;
    font-weight: normal;
    color:#C613F2;
}

.number {
    letter-spacing: 2px;
    background: #f5f5f5;
    padding: 10px 20px;
    border-radius: 20px;
}
body{
  background-color: #fffacd
}


/* 애니메이션 */


</style>