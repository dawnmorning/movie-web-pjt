<template>
  <div style='position:related; margin-top:170px;'>
    <!-- 로그인 시 보일 화면 -->
    <div v-if='isLogin' >
      <div class='jua animate__animated animate__backInUp delay-4s' style='color:black; margin-top:100px;'>
        <div class=''>안녕하세요, {{ nickname }} 님</div> 
        <div class='mt-5 ' >오늘 기분은 어때요?</div>
        <b-button style='background-color: white;' @click='goRecommend' class='btn btn-outline-primary btn-lg'><span>영화를 고르러 가볼까요?</span> </b-button>
      </div>
      <div>
        <div class="today jua " style='display:inline; position:related; right:1200px;'>
            <div class='visitor animate__animated animate__heartBeat animate__repeat-3 delay-4s'>
                <p>오늘 방문자 수</p>
                <number class="number" :from="0" :to="16823405" :duration="500"/>
            </div>
        </div>
      </div>
    </div>
    <!-- 비로그인 시 보일 화면 -->
    <div v-if='!isLogin'>
      <LogIn/>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
const DJANGO_URL='http://127.0.0.1:8000'
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
    },
    getMovieTitle() {
        this.$store.dispatch('getMovieTitles')
    },
    getRandomMovies(){
        axios({
            method: 'get',
            url: `${DJANGO_URL}/api/v2/movies/random/`,
            headers: { Authorization : `Token ${this.$store.state.token}` }
        })
        .then(res => {                
            this.randomMovies = res.data
        })
        .catch(err => { console.log(err) })
      },     
  },
  created(){
        this.getMovieTitle()
        this.$store.dispatch('getMovies')
        this.getRandomMovies()
  }
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