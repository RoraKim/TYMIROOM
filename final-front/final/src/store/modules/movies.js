import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

export default {

  state: {
    movies: [],
    actors:[],
    actor:[],
    movie: [],
    recommendation: [],
    star: '3'
  },
  getters: {
    // movie
    movies: state => state.movies,
    movie: state => state.movie,

    // actor
    actors: state => state.actors,
    actor: state => state.actor,

    recommendation: state => state.recommendation,
    star: state => state.star
  },
  // state의 값을 변경해줌, actions에서 commit()으로 호출됨
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,

    SET_ACTORS: (state, actors) => state.actors = actors,
    SET_ACTOR: (state, actor) => state.actor = actor,

    SET_RECOMMENDATION: (state, recommendation) => state.recommendation = recommendation,
    SET_STAR(state, star) {
      state.star = star
    }
  },
  actions: {
    fetchMovies({ commit, getters }, {search, random, date, page}) {
      let query = "?"
      if (search) {
        query += `search=${search}`
      }
      if (random) {
        query += `&random=${random}`
      }
      if (date) {
        query += `&date=${date}`
      }
      if (page) {
        query += `&page=${page}`
      }

      axios({
        url: drf.movies.movies() + query,
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },

    fetchWishMovies({ commit }, wishMovies) {
      commit('SET_MOVIES', wishMovies)
    },

    // 영화 월드컵 가져오기
    fetchMovieGames({ commit, getters }) {
      axios({
        url: drf.movies.moviegames(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },
    // 배우 월드컵 가져오기
    fetchActorGames({ commit, getters }) {
      axios({
        url: drf.movies.actorgames(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_ACTORS', res.data))
        .catch(err => console.error(err.response))
    },
    
    // 장르별 영화 가져오기
    fetchGenreMovies({ commit, getters }, genreId) {
      axios({
        url: drf.movies.genreMovies(genreId),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },

    fetchMovie({ commit, getters }, movieId) {
      axios({
        url: drf.movies.movieDetail(movieId),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))    
    },

    fetchActor({ commit, getters }, actorId) {
      axios({
        url: drf.movies.actorDetail(actorId),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => commit('SET_ACTOR', res.data))
        .catch(err => console.error(err.response))    
    },

    fetchRecommendation({ commit }, movieId) {
      axios({
        url: `https://api.themoviedb.org/3/movie/${movieId}/recommendations?api_key=a019e211e4eb80411e10424e9f75bc1d&language=ko&page=1`,
        method: 'get',
      })
      .then(res => commit('SET_RECOMMENDATION', res.data))
      .catch(err => console.error(err.response))
    },

    fetchMyMovies({ commit, getters }, username) {
      axios({
        url: drf.movies.seenMovies(username),
        method: 'get',
        headers: getters.authHeader
      })
      .then(res => commit('SET_MOVIES', res.data))
      .catch(err => console.error(err.response))
    },

    wishMovie({ commit, getters }, movieId) {
      axios({
        url: drf.movies.wishMovieUpdate(movieId),
        method: 'post',
        headers: getters.authHeader
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },

    seenMovie({ commit, getters }, movieId) {
      axios({
        url: drf.movies.seenMovieUpdate(movieId),
        method: 'post',
        headers: getters.authHeader
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },

    createReview({ commit, getters }, { movieId, content, score }) { 
      axios({
        url: drf.movies.movieDetail(movieId),
        method: 'post',
        data: {content, score},
        headers: getters.authHeader
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },

    updateReview({ commit, getters }, { movieId, reviewId, content, score }) {
      axios({
        url: drf.movies.reviewUpdate(movieId, reviewId),
        method: 'put',
        data: {content, score},
        headers: getters.authHeader
      })
      .then(res => commit('SET_MOVIE', res.data))
      .catch(err => console.error(err.response))
    },

    deleteReview({ commit, getters }, { movieId, reviewId }) {
      axios({
        url: drf.movies.reviewUpdate(movieId, reviewId),
        method: 'delete',
        data: {},
        headers: getters.authHeader
      })
      .then(res => commit('SET_MOVIE', res.data))
      .catch(err => console.error(err.response))
    },

    likeReview({ commit, getters }, { movieId, reviewId }) {
      axios({
        url: drf.movies.reviewLike(movieId, reviewId),
        method: 'post',
        data: {},
        headers: getters.authHeader
      })
      .then(res => commit('SET_MOVIE', res.data))
      .catch(err => console.error(err.response))
    },
    fetchStar({ commit }, star) {
      commit('SET_STAR', star)
    }
  }
}