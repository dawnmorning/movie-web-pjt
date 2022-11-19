<template>
  <div id="app">
    <!-- 로그인 후 -->
    <span>
      <nav class="sticky-top navbar navbar-expand-lg navbar-light bg-light ">
        <div class="container-fluid">
          <a class="navbar-brand fs-1" href="#">우리 프로젝트 명</a>
          
          <div v-if="isLogin">
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
                  <router-link class='nav-link' :to="{name: 'HomeView'}">홈</router-link>
                  <!-- <a class="nav-link active" aria-current="page" href="http://localhost:8080/">홈</a> -->
                </li>
                <li class="nav-item">
                  <router-link class='nav-link' :to="{name: 'CommunityView'}">커뮤니티</router-link>
                  <!-- <a class="nav-link" href="/community">커뮤니티</a> -->
                </li>
                <li class="nav-item">
                  <router-link class='nav-link' :to="`/profile/${this.$store.state.username}`">내 프로필</router-link>
                  <!-- <a class='nav-link' :href="`/profile/${username}`">내 프로필</a> -->
                </li>
                <li class="nav-item">
                  <a @click='noToken' class="nav-link" href="#">로그아웃</a>
                </li>
              </ul>
            </div>
          </div>

        </div>
      </nav>
    </span>
    <!-- 로그인 전 -->
    
    <!-- <nav v-if ='!isLogin'>
      <LogIn/>
    </nav> -->

    <router-view/>
  </div>
</template>

<script>
// import LogIn from '@/components/LogIn'

export default {
  name: 'App',
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
    // username(){
    //   return 
    // }
  // components:{
  //   LogIn,
  // }
}
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  justify-content: center;
} */

/* nav {
  padding: 30px;
} */

nav a {
  font-weight: bold;
  color: #2c3e50;
}
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

/* nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
