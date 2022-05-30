import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import HomeView from '../views/HomeView.vue'
import MovieRecommendationView from '../views/MovieRecommendationView.vue'
import MyMovieView from '../views/MyMovieView.vue'
import MiniGameView from '../views/MiniGameView.vue'
import FriendSearchView from '../views/FriendSearchView.vue'
import UserSearchView from '../views/UserSearchView.vue'
import MySettingsView from '../views/MySettingsView.vue'
import MyProfileSettingsView from '../views/MyProfileSettingsView.vue'
import NotFound404 from '../views/NotFound404.vue'

import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import LogoutView from '../views/LogoutView.vue'
import ActorGameView from '../views/ActorGameView.vue'
import MovieGameView from '../views/MovieGameView.vue'
import TestGameView from '../views/TestGameView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home/:username',
    name: 'home',
    component: HomeView
  },
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/movies/recommend',
    name: 'recommend',
    component: MovieRecommendationView
  },
  {
    path: '/movies/mymovie/:username',
    name: 'mymovie',
    component: MyMovieView
  },
  {
    path: '/movies/minigame',
    name: 'minigame',
    component: MiniGameView
  },
  {
    path: '/movies/minigame/moviegame',
    name: 'Moviegame',
    component: MovieGameView
  },
  {
    path: '/movies/minigame/actorgame',
    name: 'Actorgame',
    component: ActorGameView
  },
  {
    path: '/movies/minigame/testgame',
    name: 'Testgame',
    component: TestGameView
  },
  {
    path: '/movies/friends',
    name: 'friends',
    component: FriendSearchView
  },
  {
    path: '/movies/user/search',
    name: 'usersearch',
    component: UserSearchView
  },
  {
    path: '/movies/settings',
    name: 'settings',
    component: MySettingsView
  },
  {
    path: '/movies/settings/profile',
    name: 'profileSettings',
    component: MyProfileSettingsView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup']

  const isAuthRequired = !noAuthPages.includes(to.name)
  

  if (isAuthRequired && !isLoggedIn) {
    alert('로그인이 필요합니다.')
    next({ name: 'login' })
  } else {
    next()
  }
})


export default router
