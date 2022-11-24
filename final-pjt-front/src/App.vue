<template style=' background-color: #f5f5f5;'>
  <body style=' background-color: #f5f5f5'>
    <div id="app  background-color: #f5f5f5;">
      
      <!-- 로그인 후 -->
      <span v-if='isLogin' style=' background-color: #f5f5f5;'>
        <nav class="navbar fixed-top navbar navbar-expand-lg navbar-light bg-light " style=' background-color: #f5f5f5'>
          <div class="container-fluid jua " style='margin-top:0px; width:1300px; background-color: #f5f5f5;' >
            <router-link style='width:600px; ' class="navbar-brand fs-1" :to='{name: "HomeView"}'><img src="http://127.0.0.1:8000/media/final_logo2.jpg" style='width:28%;'></router-link>

            <div class="justify-content-end collapse navbar-collapse " id="navbarSupportedContent">

            <div v-if="movieTitles" style=''> 
              <SearchAutocomplete
                style="width: 300px; border-color:rgba(255,255,255,0.1); position:relative; right:150px; border:none; padding:0;  background-color: #f5f5f5;"
                class="form-control"
                :items="movieTitles"
                @selected-movie="goMovieCard"
              />
            </div>

              <ul class="nav justify-content-end fs-6">
                <li class="nav-item">
                  <router-link style='color:27AEF5;' class='nav-link' :to="{name: 'HomeView'}">홈</router-link>
                  
                </li>
                <li class="nav-item">
                  <router-link  style='color:27AEF5;' class='nav-link' :to="{name: 'CommunityView'}">커뮤니티</router-link>
                  
                </li>
                <li class="nav-item">
                  <!-- <router-link class='nav-link' :to="`/profile/${this.$store.state.username}`">내 프로필</router-link> -->
                  <a class='nav-link'  style='color:27AEF5;' :href="`http://localhost:8080/profile/${this.$store.state.username}`">내 프로필</a>
                  
                </li>
                <li class="nav-item">
                  <a @click='logOut'  style='color:27AEF5;' class="nav-link" href="#">로그아웃</a>
                </li>
                
              </ul>
              
            </div>
          </div>
        </nav>
      </span>
      <router-view/>
    </div>
  </body>

</template>

<script>
// import LogIn from '@/components/LogIn'
import SearchAutocomplete from './components/SearchAutocomplete.vue'

export default {
  name: 'App',
  data() {
    return {
      result: null,
    }
  },
  components: {
    SearchAutocomplete
  },
  computed:{
    username() {
        return this.$store.state.username
      },
      isLogin(){
          return this.$store.getters.isLogin
      },
      movieTitles() {
        return this.$store.state.movieTitles.map(movietitle => {
          return movietitle.title
        })
      }
  },
  methods:{
    // movieInput(event) {
    //   const inputData = event.taget.value
    //   const autocomplete = document.querySelector(".autocomplete");
    //   console.log(inputData)
    //   if (inputData) {
    //     autocomplete.classList.remove("disabled");
    //     this.result = this.movieTitles.filter((title) => {
    //       return title.title.includes(inputData)})
    //   } else {
    //     autocomplete.classList.add("disabled");
    //   }
    // },
    goMovieCard(movietitle) {
      const movie = this.$store.state.movieTitles.find(movieTitles => {
        return movieTitles.title === movietitle
      })
      this.$router.push({name: 'PostReview', params:{movie_id: movie.id}})

    },
    logOut(){
      this.$store.dispatch('logOut')
      
    },
    goRecommend(){
      this.$router.push({name: "RecomView"})
    },
    getMovieTitle() {
      this.$store.dispatch('getMovieTitles')
    }
  },
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
  color: black;
} 

nav{
  position: fixed;
  top: 0;
  height: 70px;
  left: 0;
  right: 0;
  margin:0 auto;
}
#app{
 background-color: #f5f5f5
}
/* nav a.router-link-exact-active {
  color: #42b983;
} */

router-link{
  color: green;
}
</style>
