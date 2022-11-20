import Vue from 'vue'
import VueRouter from 'vue-router'

import SignUp from '@/components/SignUp'
import LogIn from '@/components/LogIn'
import PostReview from '@/components/PostReview'
import ReviewDetail from '@/components/ReviewDetail'

import HomeView from '@/views/HomeView'
import testView from '@/views/testView'
<<<<<<< HEAD
import EditProfileView from '@/views/EditProfileView'
=======
import RecomView from '@/views/RecomView'
import ProfileView from '@/views/ProfileView'
import EditProfile from '@/views/EditProfile'
>>>>>>> 5f366e8cda8e2be596368a12807df0fcd966c854
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
    name: 'EditProfileView',
    component: EditProfileView,
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/post/review/:movie_id',
    name: 'PostReview',
    component: PostReview
  },
  {
    path: '/review/detail',
    name: 'ReviewDetail',
    component: ReviewDetail
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
