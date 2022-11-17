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
      }
  },
  
  modules: {
  }
})

