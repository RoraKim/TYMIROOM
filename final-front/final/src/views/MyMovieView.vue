<template>
<div id="outer" v-if="this.profile.profile_set">
 <!-- <div class="home back d-flex justify-content-center align-items-center pb-5"> -->
  <div class="d-flex p-2" style="height: 84vh; width: 74%; background-color:#EA8D98;" id="inner" v-if="currentUser.username === this.$route.params.username">
       
       <!-- 왼쪽 핑크 박스 -->
    <div class="d-flex p-5 m-2" style="height: 80vh; width: 25%; background-color:#F9EEF5;" id="border">
      <div class = "d-flex justify-content-center row">
        <!-- 티미 사진 -->
        <div class="border cards" style="height:250px; width: 250px; background-color:#FCFEFF; padding:0; box-shadow:none;">
          <img :src="require('../assets/tymi_profile/'+ profile.profile_set[0].tymi_image + '_profile.png')" style="height:250px; width: 250px;">
         </div>

         <!-- 내 팝콘 레벨 -->
          <div class="sub ms-4" style="height: 100px;">
            <div v-if="profile.profile_set[0].level === 0">
              <img :src="require('../assets/popcorn/level'+ profile.profile_set[0].level + '.png')" 
              class="inline" style="width: 50px; display: inline-block;">
              <h4 class="inline" style="margin: 10px; width: 30px; display: inline-block;">  lv.{{ profile.profile_set[0].level + 1 }}</h4>
              <p class="m-0 px-3">남긴 리뷰 수 : {{ profile.profile_set[0].exp }} / 10 exp</p>
              <div class="progress" style="height: 8px; background: #C4C4C4; width: 90%" >
                <div class="progress-bar" role="progressbar" :style="'width: ' + profile.profile_set[0].exp * 10 + '%; background: #EA8D98;'"></div>
              </div>
            </div>
            <div v-else>
              <img :src="require('../assets/popcorn/level'+ profile.profile_set[0].level + '.png')" 
              class="inline" style="width: 50px;">
              <h4 class="inline" style="margin: 10px; width: 30px; display: inline-block;">  lv.MAX</h4>
              <h5 class="m-0 p-2">남긴 리뷰 수 : {{ profile.profile_set[0].exp }}</h5>
            </div>
          </div>

                     <!-- 내 인생영화 -->
          <div class="sub ms-4">
            <img src="../assets/slate.png" style="width: 50px; display: inline-block;"><h4 class="inline" style="margin: 10px; width:80px; display: inline-block">인생영화</h4>
            <h5 v-if="profile.profile_set[0].life_movie" class="ms-2">
              {{ profile.profile_set[0].life_movie }}
            </h5>
            <h5 v-else class="ms-2">
              인생 영화가 없어요,,
            </h5>
          </div>

          <!-- 내 홈으로 가기 -->
          <a :href="'http://localhost:8080/home/'+currentUser.username" style="text-decoration: none; color: black" class="sub mb-3 ms-4">
            <img src="../assets/home.png" class="inline" style="width: 45px;">
            <h5 class="ms-2">내 티미룸으로 가기</h5>
          </a>
        </div>
      </div>
    <!-- 오른쪽 박스 -->
    <div style="height: 80vh; width: 75%; overflow:scroll; background-color: white;" class="p-5 m-2" id="border">
      <h1 class="fw-bold">내 영화</h1>
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
                  <div class="modal-body" >
                    <movie-detail :movieId="movie.movie_id"></movie-detail>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>                  </div>
                </div>
              </div>
            </div>

        </div>
      </div>
    </div>

      <div class="ms-auto" style="height: 80vh; width: 0%;">
        <router-link :to="{ name: 'home', params: {username: currentUser.username} }" class="link_active"><button class="top-btn btn btn-light mb-2 rounded-end fs-4">홈</button></router-link>
        <router-link to="/movies/recommend" class="link"><button class="btn btn-light my-2 rounded-end fs-4">추천영화</button></router-link>
        <router-link :to="{ name: 'mymovie', params: {username: currentUser.username} }" class="link"><button class="btn-light my-2 rounded-end fs-4">내 영화</button></router-link>
        <router-link to="/movies/minigame" class="link"><button class="btn btn-light my-2 rounded-end fs-4">미니게임</button></router-link>
        <router-link to="/movies/friends" class="link"><button class="btn btn-light my-2 rounded-end fs-4">친구관리</button></router-link>
        <router-link to="/movies/settings" class="link"><button class="btn btn-light my-2 rounded-end fs-4">설정</button></router-link>    
      </div>
     </div>
 

  <!-- 친구 -->
    <div class="d-flex p-2" style="height: 84vh; width: 74%; background-color: #a2d2ff;" id="inner" v-else>

      <div class="d-flex p-5 m-2" style="height: 80vh; width: 25%; background-color:#dceef3;" id="border">
      <div class = "d-flex justify-content-center row">
        <!-- 티미 사진 -->
        <div class="border cards" style="height:250px; width: 250px; background-color:#FCFEFF; padding:0; box-shadow:none;">
          <img :src="require('../assets/tymi_profile/'+ profile.profile_set[0].tymi_image + '_profile.png')" style="height:250px; width: 250px;">
        </div>
        
        <div class="sub d-flex justify-content-center" v-if="this.followers.followings">
          <div style="height:60px;"></div>
        </div>

         <!-- 내 인생영화 -->
        <div class="sub ms-4">
          <img src="../assets/slate.png" style="width: 50px;"><h4 class="d-inline" style="margin: 10px">인생영화</h4>
          <h5 v-if="profile.profile_set[0].life_movie" class="ms-2">
            {{ profile.profile_set[0].life_movie }}
          </h5>
          <h5 v-else class="ms-2">
            인생 영화가 없어요,,
          </h5>
        </div>

        <!-- 내 홈으로 가기 -->
        <a :href="'http://localhost:8080/home/'+currentUser.username" style="text-decoration: none; color: black" class="sub mb-3 ms-4">
          <img src="../assets/home.png" class="inline" style="width: 45px;">
          <h5 class="ms-2">내 티미룸으로 가기</h5>
        </a>





        <!-- 친구 파도타기 -->
        <select class="form-select form-select mb-3 fs-4" style="height: 50px;" onchange="location.href=(value);">
          <option selected value="none">친구 파도타기</option>
          <option v-for="friend in this.followers.followers" :key="friend.id" :value="'http://localhost:8080/home/'+friend.username">{{ friend.username }}</option>
        </select>
      </div>
    </div>

    <div style="height: 80vh; width: 75%; overflow:scroll; background-color: white;" class="p-5 m-2" id="border">
      <h1 class="fw-bold">{{ profile.username }} 님의 영화</h1>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col" v-for="movie in movies" :key="movie.id">
          <div class="card shadow">
            <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" class="card-img-top" alt="..." style="height: 400px;">
            <div class="card-body">
              <h3 class="card-title text-center">{{ movie.title }}</h3>
              <p class="card-title text-center">{{ movie.release_date }}</p>
            </div>
            <a href="" class="stretched-link" data-bs-toggle="modal" :data-bs-target="'#staticBackdrop' + movie.movie_id" @click="[fetchMovie(movie.movie_id), fetchRecommendation(movie.movie_id)]"></a>
          </div>

            <div class="modal fade" :id="'staticBackdrop' + movie.movie_id" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable modal-xl">
                <div class="modal-content">
                  <div class="modal-body" >
                    <movie-detail :movieId="movie.movie_id"></movie-detail>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>                  
                  </div>
                </div>
              </div>
            </div>

        </div>
      </div>
    </div>

    <div class="ms-auto" style="height: 80vh; width: 0%;">
      <router-link :to="{ name: 'home', params: {username: this.$route.params.username} }" class="link"><button class="top-btn btn btn-light mb-2 f-rounded-end fs-4">홈</button></router-link>
      <router-link :to="{ name: 'mymovie', params: {username: this.$route.params.username} }" class="link"><button class="btn btn-light my-2 f-rounded-end fs-5" style="background-color:white;">친구의영화</button></router-link>
    </div>
  </div>

 </div>
</template>



<script>
import { mapGetters, mapActions } from 'vuex'
import MovieDetail from '@/components/MovieDetail.vue'

export default {
  name: 'MovieRecommendationView',
  components: { MovieDetail },
  computed: {
    ...mapGetters([ 'profile', 'currentUser', 'followers', 'currentUser', 'movies', 'profile'])
  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchCurrentUser', 'follow', 'fetchFollowers', 'fetchMyMovies', 'fetchMovie', 'fetchRecommendation', 'fetchCurrentUser', 'fetchProfile'])
  },
  created() {
    this.fetchCurrentUser(), 
    this.fetchMyMovies(this.$route.params.username),
    this.fetchProfile(this.$route.params.username),
    this.fetchFollowers(this.$route.params.username)
  }
}

</script>

<style>
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
</style>
