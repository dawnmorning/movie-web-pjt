import Vue from 'vue'
import VueRouter from 'vue-router'

import SignUp from '@/components/SignUp'
import LogIn from '@/components/LogIn'
import HomeView from '@/views/HomeView'
import ProfileView from '@/views/ProfileView'
import RecomView from '@/views/RecomView'
import testView from '@/views/testView'
import EditProfile from '@/views/EditProfile'
import CommunityView from '@/views/CommunityView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/home',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/profile/:username',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/recommendation',
    name: 'RecomView',
    component: RecomView
  },
  {
    path: '/test',
    name: 'testView',
    component: testView
  },
  {
    path: '/edit/:username',
    name: 'EditProfile',
    component: EditProfile
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
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
