import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import router from '@/router'
import createPersistedState from 'vuex-persistedstate'

const DJANGO_URL='http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    token: null,
    username: null,
    reviews:null,  
  },

  getters: {
    isLogin(state){
      return state.token ? true : false
    }
  },
  mutations: {
    SAVE_TOKEN(state, data){
      state.username = data.username
      state.token = data.token
    },
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
    signUp(context, payload) {
      // console.log(context, payload)
      axios({
        method: 'post',
        url: `${DJANGO_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          // console.log(res)
          const data = {
            token : res.data.key,
            username: payload.username
          }
          context.commit('SAVE_TOKEN', data)
        
        })
    },
    
    logIn(context, payload){
      console.log(context, payload)
      axios({
        method:'post',
        url: `${DJANGO_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then(res => {
          const data = {
            token : res.data.key,
            username: payload.username
          }
          context.commit('SAVE_TOKEN', data)
          
        })
        .catch(err => {
          console.error(err)
        })
    },

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

