<template>
  <div>
    <!-- 로그인 시 보일 화면 -->
    <div v-if='isLogin'>
      <TheHome/>
    </div>
    <div v-if='!isLogin'>
      <LogIn/>
    </div>
  </div>
</template>

<script>
import LogIn from '@/components/LogIn'
import TheHome from '@/components/TheHome'
export default {
    name: 'HomeView',
    components:{
      LogIn,
      TheHome
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