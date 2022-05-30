<template>
<div id="outer">
 <div class="d-flex p-2" style="height: 84vh; width: 74%; background-color:#EA8D98;" id="inner">

  <!-- 왼쪽 박스 -->
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
  <div style="height: 80vh; width: 75%; overflow:scroll;" class="p-5 pb-2 m-2" id="border">
    <h1 class="fw-bold"> 미니 게임</h1>
    <hr style="width: 900px">
    <div class="d-flex row justify-content-center m-5">
      <div class="d-flex justify-content-evenly">
        <router-link to="/movies/minigame/actorgame" class="link game" style="display: inline-block; background-color: white"><img src="../assets/actorgame1.png" class="gameimg" alt="" @click="randomActorCall()" style="display: inline-block;">
        <h4 style="color: black; margin-top: 20px; margin-left: 20px"> 배우 월드컵 </h4>
        </router-link>

        <router-link to="/movies/minigame/moviegame" class="link game" style="display: inline-block; background-color: white"><img src="../assets/moviegame.png" class="gameimg" style="display: inline-block;">
          <h4 style="color: black; margin-top: 20px; margin-left: 20px"> 영화 월드컵 </h4>
        </router-link>

        <router-link to="/movies/minigame/testgame" class="link game" style="display: inline-block; background-color: white" ><img src="../assets/testgame.png" class="gameimg" style="display: inline-block;">
          <h4 style="color: black; margin-top: 20px; margin-left: 30px"> 심리테스트 </h4>
        </router-link>
      </div>

      <!-- 게임 이미지 -->
      <img src="../assets/minigame.png" class="p-0 m-0" alt="" style="width: 750px; margin-left: 30px, padding:0px" id="border">
    </div>
  </div>

    <div class="ms-auto" style="height: 80vh; width: 0%;">
      <router-link :to="{ name: 'home', params: {username: currentUser.username} }" class="link_active"><button class="top-btn btn btn-light mb-2 rounded-end fs-4">홈</button></router-link>
      <router-link to="/movies/recommend" class="link"><button class="btn btn-light my-2 rounded-end fs-4">추천영화</button></router-link>
      <router-link :to="{ name: 'mymovie', params: {username: currentUser.username} }" class="link"><button class="btn btn-light my-2 rounded-end fs-4">내 영화</button></router-link>
      <router-link to="/movies/minigame" class="link"><button class="btn-light my-2 rounded-end fs-4">미니게임</button></router-link>
      <router-link to="/movies/friends" class="link"><button class="btn btn-light my-2 rounded-end fs-4">친구관리</button></router-link>
      <router-link to="/movies/settings" class="link"><button class="btn btn-light my-2 rounded-end fs-4">설정</button></router-link>    
    </div>
  </div>
</div>

</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile', 'movies','actors','currentUser'])
  },
  methods: {
    ...mapActions(['fetchActorGames', 'fetchMovieGames', 'fetchProfile', 'fetchCurrentUser']),
  },
  created() {
    this.fetchProfile(this.currentUser.username),
    this.fetchMovieGames(),
    this.fetchActorGames()
  },
}

</script>

<style scoped>
.back {
  background-color: #EA8D98;
  border: 4px dashed #FCFEFF;
  background-size: 100%;
  height: 100vh;

}
.bg-light {
  margin: 100px;
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
  background-color: #dceef3;
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

.gameimg {
  width: 150px;
  height: 150px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;

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

#border { 
/* box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25); */
border-radius: 10px;
background-color: white;
}

.btn { 
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
  height: 40px; width: 90px;
}

.dashed{
  width:85%;
  height: 95vh;
  /* border: 4px dashed white; */
  position: absolute;
  border-radius: 10px;
  left: 10%;
  right: 10%;
  top: 5%;
  overflow: hidden;
  padding: 10px;
  background-color: #EA8D98;
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

.home{
  /* width: 70%;
  height: 70%; */
  margin: 10px;
}

#outer{
  border-color: #EA8D98;
  border-width:20px;
  margin-left: 200px;
  margin-top: 60px;
}

.gamebtn{
 width: 200px;
 height: 100px;
 margin-bottom: 50px;
 /* margin-top: 100px; */
}

.search { 
  width: 70px;
  margin: 15px;

}

.inline { 
  display: inline-block;
}

.game {
  margin: 73px;
  /* margin-left: 100px; */
  margin-top: 0px;
  margin-bottom: 20px;

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
