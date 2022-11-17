import Vue from 'vue'
import VueRouter from 'vue-router'

import SignUp from '@/views/SignUp'
import HomeView from '@/views/HomeView'
import Myprofile from '@/views/MyProfile'
import RecomView from '@/views/RecomView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/profile/:username',
    name: 'MyProfile',
    component: Myprofile
  },
  {
    path: '/recommendation',
    name: 'RecomView',
    component: RecomView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// 로그아웃 시 NavigationDuplicated 에러
// https://velog.io/@hschoi1104/Vue.js-NavigationDuplicated-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0%ED%95%98%EA%B8%B0
const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => {
		if (err.name !== 'NavigationDuplicated') throw err;
	});
};

export default router
