import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import _ from 'lodash'

import createPersistedState from 'vuex-persistedstate'

const DJANGO_URL='http://127.0.0.1:8000'


Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    // 유저 관련 정보
    token: null,
    user_id: null,
    username: null,
    nickname: null,
    profile_image: null,
    // 영화 관련 데이터
    latest_movies: null,
    popular_movies: null,
    random_movies: null,
    upcomming_movies: null,
    vote_movies: null,
    movie_detail: null,
    // 커뮤니티 관련 함수
    reviews:null,
  },

  getters: {
    isLogin(state){ return state.token ? true : false },
    random_movies_10(state) { return _.sampleSize(state.random_movies, 10) },
  },

  mutations: {
    SAVE_TOKEN(state, token){
      state.token = token
    },

    GET_PROFILE(state, data) {
      state.user_id = data.id
      state.username = data.username
      state.nickname = data.nickname
      state.email = data.email
      state.profile_image = data.profile_image
      state.grade = data.grade
    },

    LOGOUT(state) {
      state.user_id = null
      state.token = null
      state.username = null
      state.nickname = null
      state.profile_image = null
      state.grade = null
      localStorage.clear()
      router.push({name: "LogIn"})
    },

    // movies 관련 함수
    GET_MOVIES(state, MoviesData){     
      state.upcomming_movies = MoviesData.upcomming_movies
      state.latest_movies = MoviesData.latest_movies   
      state.popular_movies = MoviesData.popular_movies
      state.random_movies = MoviesData.random_movies
      state.vote_movies = MoviesData.vote_movies
    },

    GET_MOVIE_DETAIL(state, MoviesData){ 
      state.movie_detail = MoviesData
    },

    // community 관련 함수
    GET_REVIEWS(state, reviews){
      state.reviews = reviews
    },

    DELETE_COMMENT(state, comment){
      state.reviews = state.reviews.map( review => {
        if (review.id === comment.review) {
          review.comments = review.comments.filter( commentInState => {
            return commentInState.id != comment.id
          })
        }
        return review
      })
    },
    // {
    //   "id": 7,
    //   "content": "저랑 취향이 갈리네요 !",
    //   "review": 7,
    //   "author": 1,
    //   "like_users": []
    // }
    CREATE_COMMENT(state, comment) {
      state.reviews = state.reviews.map(review => {
        if (review.id == comment.review) { review.comments.push(comment) }
        return review
      })      
    }
    
  },
  actions: {
    // account 관련 함수
    getProfile(context, data){
      
      axios({
        method: 'get',
        url : `${DJANGO_URL}/api/v1/${data.username}/`,
        headers:{
          Authorization : `Token ${data.token}`,
        },
      })
      .then(res => { 
        context.commit('GET_PROFILE', res.data)
      })
      .catch( err => console.log(err))
    },

    signUp(context, payload) {
      // console.log(context, payload)
      axios({
        method: 'post',
        url: `${DJANGO_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          nickname: payload.nickname,
          email: payload.email,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
      .then(res => {
        // console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
        alert('회원가입이 완료되었습니다.')
        const data = {
          token: res.data.key,
          username: payload.username
        }
        context.dispatch('getProfile', data)
        router.push({name:'HomeView'})
      })
      .catch( function(err) {
        console.log(err)
        router.push({ name:'SignUp', query:err })
      })
    },
    
    logIn(context, payload){
      axios({
        method:'post',
        url: `${DJANGO_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
      .then(res => {
        context.commit('SAVE_TOKEN', res.data.key)

        const data = {
          token: res.data.key,
          username: payload.username
        }
        context.dispatch('getProfile', data)
        router.push({name: 'HomeView'})
      })
      .catch(err => {
        console.error(err)
      })
    },

    logOut(context){
      axios({
        method:'post',
        url: `${DJANGO_URL}/accounts/logout/`,
        headers:{
          Authorization : `Token ${context.state.token}`,
        },
      })
      .then(() => {
        context.commit('LOGOUT')
        console.log('logout')
      })
      .catch(err => {
        console.error(err)
      })
    },

    // movies 관련 함수
    getMovies(context){
      axios({
          method: 'get',
          url: `${DJANGO_URL}/api/v2/movies/`,
          headers: { Authorization : `Token ${context.state.token}` }
      })
      .then(res => {
        context.commit('GET_MOVIES', res.data)
      })
      .catch(err => { console.log(err) })
    },

    getMovieDetail(context, payload){
      axios({
          method: 'get',
          url: `${DJANGO_URL}/api/v2/${payload.movie_id}/movies/`,
          headers: { Authorization : `Token ${context.state.token}` }
      })
      .then(res => {
        context.commit('GET_MOVIE_DETAIL', res.data)
      })
      .catch(err => { console.log(err) })
    },
  
    // community
    getReviews(context){
      axios({
        method: 'get',
        url:`${DJANGO_URL}/api/v3/reviews/`,
        headers:{
          Authorization : `Token ${context.state.token}`,
        },
      })
      .then(res => {
        const reviews = res.data // Array
        context.commit('GET_REVIEWS', reviews)
      })
      .catch(err => { console.log(err)})
    },
    
    // getReviewDetail(context, payload){
    //   axios({
    //     method: 'get',
    //     url:`${DJANGO_URL}/api/v3/review/`,
    //     headers:{
    //       Authorization : `Token ${context.state.token}`,
    //     },
    //   })
    //   .then(res => {
    //     const reviews = res.data // Array
    //     context.commit('GET_REVIEWS', reviews)
    //   })
    //   .catch(err => { console.log(err)})
    // },

    postReview(context, payload) {
      axios({
        method: 'post',
        url: `${DJANGO_URL}/api/v3/review/create/${payload.movie_id}/`,
        headers:{
          Authorization : `Token ${context.state.token}`,
        },
        data: {
          title: payload.title,
          content: payload.content,
          rating: payload.rating,
        }
      })
      .then(() => {
        router.push({ name : 'CommunityView'})
      })
      .catch(err => console.log(err))
    },

    deleteComment(context, comment) {
      axios({
          method: 'delete',
          url: `${DJANGO_URL}/api/v3/comment/delete/${comment.id}/`,
          headers: { Authorization : `Token ${context.state.token}`,},
      })
      .then(() => { 
        context.commit('DELETE_COMMENT', comment)
      })
      .catch(err => {
        if (err.response.status === 401) {
          alert('해당 작업의 권한이 없습니다.')
        }
      })
    },

    createComment(context, payload) {
      axios({
        method: 'post',
        url: `${DJANGO_URL}/api/v3/comment/create/${payload.review_id}/`,
        headers: { Authorization : `Token ${context.state.token}`,},
        data: {
          content: payload.comment,
        }
      })
      .then(res => {
        context.commit('CREATE_COMMENT', res.data)
      })
    }

  },
  modules: {
  }
})

