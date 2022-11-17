<template>
  <div id="app">
    <!-- 로그인 후 -->
    <nav v-if='isLogin'>
      
    </nav>
    <!-- 로그인 전 -->
    
    <nav v-if ='!isLogin'>
      <!-- <router-link :to="{name: 'LogInView'}">로그인</router-link>  -->
      <!-- <router-link :to="{name: 'SignUp'}">회원가입</router-link> -->
    </nav>
    <router-view/>
  </div>
</template>

<script>
// import LogIn from '@/components/LogIn'

export default {
  name: 'App',
  computed:{
    isLogin(){
      return this.$store.getters.isLogin
    },
    // username(){
    //   return 
    // }
  },
  
  components:{
    // LogIn,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* justify-content: center; */
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
