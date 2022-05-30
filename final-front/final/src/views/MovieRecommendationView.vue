<template>


<div id="outer">
 <!-- <div class="home back d-flex justify-content-center align-items-center pb-5"> -->
  <div class="d-flex p-2" style="height: 84vh; width: 74%; background-color:#EA8D98;" id="inner">
    <!-- 왼쪽 핑크 박스 -->
    <div class="d-flex p-5 m-2" style="height: 80vh; width: 25%; background-color:#F9EEF5;" id="border">
      <div class = "d-flex row justify-content-center">
        <div style="height:300px;">
          <div class="d-flex row justify-content-center m-0">
            <button class="btn rounded-end search fs-4" type="button" id="button-addon2" style="width:180px;" @click="randomMovies()">랜덤으로 정렬</button>
            <button class="btn rounded-end search fs-4" type="button" id="button-addon2" style="width:180px;" @click="nameMovies()">이름순 정렬</button>
            <button class="btn rounded-end search fs-4" type="button" id="button-addon2" style="width:180px;" @click="dateMovies()">날짜순 정렬</button>
            <button class="btn rounded-end search fs-4" type="button" id="button-addon2" style="width:180px;" @click="wishMovies()">내 위시리스트</button>
          </div>
        </div>
        <div style="height:100px;">
          <div class="input-group mb-3">
            <input type="text" class="form-control fs-4" placeholder="영화 제목" aria-label="Recipient's username" aria-describedby="button-addon2" v-model="search" @keyup.enter="searchMovies">
            <button class="btn rounded-end fs-4" style="width:70px; height: 50px;" type="button" id="button-addon2" @click="searchMovies">검색</button>
          </div>
        </div>
        <div style="width:250px; height:250px;">
          <img :src="require('../assets/movie/'+ pic + '.gif')" id="pic">
        </div>
      </div>
    </div>

    <!-- 오른쪽 메인 박스 -->
    <div style="height: 80vh; width: 75%; overflow:scroll; background-color: white;" class="p-5 m-2" id="border">
      <h1 class="fw-bold">추천영화</h1>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col" v-for="movie in movies" :key="movie.id">
          <div class="card shadow">
            <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" class="card-img-top p-2 pb-3" alt="..." style="height: 400px;">
            <div class="card-body">
              <h3 class="card-title text-center">{{ movie.title }}</h3>
              <p class="card-title text-center">{{ movie.release_date }}</p>
            </div>
            <a href="" class="stretched-link" data-bs-toggle="modal" :data-bs-target="'#staticBackdrop' + movie.movie_id" @click="[fetchMovie(movie.movie_id), fetchRecommendation(movie.movie_id)]"></a>
          </div>

            <div class="modal fade" :id="'staticBackdrop' + movie.movie_id" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable modal-xl">
                <div class="modal-content">
                  <div class="modal-body p-4" >
                    <movie-detail :movieId="movie.movie_id"></movie-detail>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="this.fetchProfile(this.currentUser.username)">Close</button>                  
                    </div>
                </div>
              </div>
            </div>
        </div>
      </div>
      <div class="d-flex justify-content-center pt-5" v-if="this.isPage">
        <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          first-number
          last-number
          page-class="customPage"
        ></b-pagination>
      </div>

    </div>
    <div class="ms-auto" style="height: 80vh; width: 0%;">
      <router-link :to="{ name: 'home', params: {username: currentUser.username} }" class="link_active"><button class="top-btn btn btn-light mb-2 rounded-end fs-4">홈</button></router-link>
      <router-link to="/movies/recommend" class="link"><button class="btn-light my-2 rounded-end fs-4">추천영화</button></router-link>
      <router-link :to="{ name: 'mymovie', params: {username: currentUser.username} }" class="link"><button class="btn btn-light my-2 rounded-end fs-4">내 영화</button></router-link>
      <router-link to="/movies/minigame" class="link"><button class="btn btn-light my-2 rounded-end fs-4">미니게임</button></router-link>
      <router-link to="/movies/friends" class="link"><button class="btn btn-light my-2 rounded-end fs-4">친구관리</button></router-link>
      <router-link to="/movies/settings" class="link"><button class="btn btn-light my-2 rounded-end fs-4">설정</button></router-link>    
    </div>
  </div>
  


  </div>
  <!-- </div> -->
</template>
<script>
import { mapGetters, mapActions } from 'vuex'
import MovieDetail from '@/components/MovieDetail.vue'
import { BPagination } from 'bootstrap-vue'
import _ from 'lodash'

export default {
  name: 'MovieRecommendationView',
  data() {
    return {
      search: '',
      currentPage: 1,
      rows: 2000,
      perPage: 18,
      isPage: true,
      date: 0,
      pic: _.sample(["1", "2", "3", "4", "5"])
    }
  },
  components: { MovieDetail, BPagination },
  computed: {
    ...mapGetters(['currentUser', 'movies', 'profile'])
  },
  methods: {
    ...mapActions(['fetchMovies', 'fetchMovie', 'fetchRecommendation', 'fetchCurrentUser', 'fetchWishMovies', 'fetchProfile']),
    searchMovies() {
      this.fetchMovies({ search: this.search })
      this.search = ''
      this.isPage = false
      this.currentPage = 1
    },
    randomMovies() {
      this.date = 0
      this.fetchMovies({ random: 1 })
      this.isPage = false
      this.currentPage = 1
    },
    dateMovies() {
      this.date = 1
      this.isPage = true
      this.currentPage = 1
      this.fetchMovies({ date: 1 })
    },
    wishMovies() {
      this.fetchWishMovies(this.profile.wish_movies)
      this.fetchProfile(this.currentUser.username)
      this.isPage = false
    },
    nameMovies() {
      this.currentPage = 1
      this.fetchMovies({ search: '' })
      this.isPage = true
    },
    pageClick() {
      console.log(this.currentPage)
      this.fetchMovies({ date:this.date, page:this.currentPage })
      console.log(this.currentPage)
    } 
  },
  watch: {
    currentPage() {
      this.pageClick()
    }
  },
  created() {
    this.fetchCurrentUser(),
    this.fetchMovies({ search: '', random: 0, date: 0}),
    this.isPage = true
  },
}

</script>

<style scoped>
.back {
  background-color: darkgrey;
  background-size: 100%;
  height: 100vh;
}
.bg-light {
  margin: 100px;
}
.btn {
  border-radius: 0rem;
}
.top-btn {
 margin-top: 60px; 
}
.link {
  text-decoration: none;
  color: white;
}
.link_active {
  text-decoration: none;
}
.card {
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}
.card:hover > img {
  /* opacity: 70%; */
  filter: brightness(20%);
  transition: opacity 1s
}
.card-body {
  position: absolute;
  width: 100%;
  color: white;
}
.card > .card-body {
  opacity: 0;
  margin-top: 40%;
  transition: opacity 0.5s
}
.card:hover > .card-body {
  opacity: 1;
  filter: brightness(100%);
}
#border { 
box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
border-radius: 10px;
}

#outer{
  border-color: #EA8D98;
  border-width:20px;
  margin-left: 200px;
  margin-top: 60px;
}
#inner{
  width:100%;
  background-color: #EA8D98;
  /* box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25); */
  border-radius: 10px;
  border: 4px dashed white;
  margin-left: 100px;
  margin-top: 70px;
}

.search { 
  width: 70px;
  margin: 15px;
}

.customPage.page-item.active .page-link {
  background-color: red;
  border-color: red;
}
.rounded-end { 
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
  height: 50px; width: 110px;
  border-radius: 0rem;
}

.f-rounded-end { 
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
  height: 50px; width: 110px;
  border-radius: 0rem;
  background-color: #bde0fe;
  border: #bde0fe;
}

#pic {
  padding: 0px;
  width: 250px;
  height: 250px;
  border: 10px outset rgb(248, 155, 170);
  border-radius: 10px;
}

</style>
