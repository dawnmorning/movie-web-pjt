<template>
  <div>
    <!-- 로그인 시 보일 화면 -->
    <div v-if='isLogin'>
        <p>Hello, {{ username }}</p>

        <router-link :to="{name: 'RecomView'}">오늘의 영화 추천 목록 보러 가기</router-link>
        <b-nav>
        <router-link :to="{name: 'HomeView'}">홈</router-link> |
        <router-link :to="`/profile/${this.$route.params.username}`">내 프로필</router-link> |
        <b-button @click='noToken'>로그아웃</b-button>
        </b-nav>
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
      localStorage.clear()
      this.$router.push({name: "HomeView"})
    }
  },
}
</script>

<style>

</style>