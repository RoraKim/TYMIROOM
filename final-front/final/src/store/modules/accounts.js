import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
import Swal from 'sweetalert2'

export default {
  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: {},
    profile: {},
    authError: null,
    followers: {},
    userlist: {}
  },

  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    followers: state => state.followers,
    userlist: state => state.userlist
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_FOLLOWERS: (state, followers) => state.followers = followers,
    SET_USERLIST: (state, userlist) => state.userlist = userlist
  },

  actions: {
    
    saveToken({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },
    removeToken({ commit }) {
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    login({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'home', params: {username: credentials.username}})
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    signup({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'home', params: {username: credentials.username}})
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    logout({ getters, dispatch }) {
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch('removeToken')
          Swal.fire({
            title: '로그아웃 성공!',
          })
          router.push({ name: 'login' })
        })
        .catch(err => {
          console.error(err.response)
        })
    },
    
    follow({ commit, getters }, username) {
      axios({
        url: drf.accounts.follow(username),
        method: 'post',
        headers: getters.authHeader
      })
      .then(res => commit('SET_PROFILE', res.data))
      .catch(err => console.error(err.response))
    },

    passwordChange({ commit, getters }, {new_password1, new_password2}) {
      axios({
        url: drf.accounts.passwordChange(),
        method: 'post',
        data: { new_password1: new_password1, new_password2: new_password2},
        headers: getters.authHeader
      })
      .then()
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },

    createGuestbook({ commit, getters }, { username, content }) {
      axios({
        url: drf.accounts.guestbook(username),
        method: 'post',
        data: {content},
        headers: getters.authHeader
      })
      .then(res => commit('SET_PROFILE', res.data))
      .catch(err => console.error(err.response))
    },
    
    updateGuestbook({ commit, getters }, { username, guestbookId, content }) {
      axios({
        url: drf.accounts.guestbookUpdate(username, guestbookId),
        method: 'put',
        data: {content},
        headers: getters.authHeader
      })
      .then(res => commit('SET_PROFILE', res.data))
      .catch(err => console.error(err.response))
    },

    deleteGuestbook({ commit, getters }, { username, guestbookId }) {
      axios({
        url: drf.accounts.guestbookUpdate(username, guestbookId),
        method: 'delete',
        data: {},
        headers: getters.authHeader
      })
      .then(res => commit('SET_PROFILE', res.data))
      .catch(err => console.error(err.response))
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => commit('SET_CURRENT_USER', res.data))
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },

    fetchProfile({ commit, getters }, username) {
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        })
        .catch(err => {
          console.error(err.response)
        })
    },

    fetchFollowers({ commit, getters }, username) {
      axios({
        url: drf.accounts.followers(username),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res =>commit('SET_FOLLOWERS', res.data))
        .catch(err => {console.error(err.response)})
    },
    
    updateProfile({ commit, getters }, {tymi, room, user, life_movie, exp, level}) {
      axios({
        url: drf.accounts.profileUpdate(),
        method: 'post',
        data: {tymi_image: tymi,room_image: room, user, life_movie, exp, level},
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_PROFILE', res.data)
      })
      .catch(err => {
        console.error(err.response)
      })
    },

    userList({ commit, getters }, username) {
      axios({
        url: drf.accounts.userList(username),
        method: 'get',
        headers: getters.authHeader
      })
      .then(res => {commit('SET_USERLIST', res.data)})
      .catch(err => {console.error(err.response)})
    }
  },
}
