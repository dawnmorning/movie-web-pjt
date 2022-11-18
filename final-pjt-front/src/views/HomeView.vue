<template>
  <div>
    <!-- 로그인 시 보일 화면 -->
    <div v-if='isLogin'>
        <p>Hello, {{ username }}</p>

        <router-link :to="{name: 'RecomView'}">오늘의 영화 추천 목록 보러 가기</router-link>

            <ul class="nav justify-content-end fs-6">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="http://localhost:8080/">홈</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">커뮤니티</a>
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
      this.$store.state.nickname = null
      this.$store.state.interested = null
      this.$store.state.profile_image = null
      localStorage.clear()
      this.$router.push({name: "HomeView"})
    }
  },
}
</script>

<style>

</style>