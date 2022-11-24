<template>
  <body style=' background-color: #f5f5f5'>
    <div id="app">
      
      <!-- 로그인 후 -->
      <span v-if='isLogin'>
        <nav class="navbar fixed-top navbar navbar-expand-lg navbar-light bg-light ">
          <div class="container-fluid jua " style='margin-top:0px; width:1300px;' >
            <router-link class="navbar-brand fs-1" :to='{name: "HomeView"}'>우리 프로젝트 명</router-link>
            <b-button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
              <input class="form-control" style="width: 200px" type="search" placeholder="Search" aria-label="Search">
            </b-button>

            <div class="justify-content-end collapse navbar-collapse " id="navbarSupportedContent">

            <div v-if="movieTitles"
> 
              <SearchAutocomplete
                style="width: 300px;"
                class="form-control"
                :items="movieTitles"
                @selected-movie="goMovieCard"
              />
            </div>

              <ul class="nav justify-content-end fs-6">
                <li class="nav-item">
                  <router-link class='nav-link' :to="{name: 'HomeView'}">홈</router-link>
                  
                </li>
                <li class="nav-item">
                  <router-link class='nav-link' :to="{name: 'CommunityView'}">커뮤니티</router-link>
                  
                </li>
                <li class="nav-item">
                  <router-link class='nav-link' :to="`/profile/${this.$store.state.username}`">내 프로필</router-link>
                  
                </li>
                <li class="nav-item">
                  <a @click='logOut' class="nav-link" href="#">로그아웃</a>
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
      console.log(movietitle)
      
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
  created() {
    this.getMovieTitle()
  }
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
</style>
