<template>
<div id="outer">
 <!-- <div class="home back d-flex justify-content-center align-items-center pb-5" style="background-color: #EA8D98;border:none;" id="border"> -->
    <div class="d-flex p-2" style="height: 84vh; width: 74%;" id="inner">

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
              class="inline" style="width: 50px; margin:5px display: inline-block">
              <h4 class="inline" style="margin: 10px">  lv.{{ profile.profile_set[0].level + 1 }}</h4>
              <p class="m-0 px-3">남긴 리뷰 수 : {{ profile.profile_set[0].exp }} / 10 exp</p>
              <div class="progress" style="height: 8px; background: #C4C4C4; width: 90%" >
                <div class="progress-bar" role="progressbar" :style="'width: ' + profile.profile_set[0].exp * 10 + '%; background: #EA8D98;'"></div>
              </div>
            </div>
            <div v-else>
              <img :src="require('../assets/popcorn/level'+ profile.profile_set[0].level + '.png')" 
              class="inline" style="width: 50px; margin:5px display: inline-block">
              <h4 class="inline" style="margin: 10px">  lv.MAX</h4>
              <h5 class="m-0 p-2">남긴 리뷰 수 : {{ profile.profile_set[0].exp }}</h5>
            </div>
          </div>

            <!-- 내 인생영화 -->
        <div class="sub ms-4">
            <img src="../assets/slate.png" style="width: 50px;"><h4 class="inline" style="margin: 10px">인생영화</h4>
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
      

      <div style="height: 80vh; width: 75%; overflow:scroll;" class="p-5 m-2" id="border">
        <h1 class="fw-bold">친구 관리</h1>
        <div class="d-flex justify-content-center">
          <router-link to="/movies/friends" class="link"><button class="btn btn-outline-secondarys fs-4 mx-4" style="width: 170px; background-color:#F5D6CB;">내 친구 관리</button></router-link>
          <router-link to="/movies/user/search" class="link"><button class="btn btn-outline-secondarys fs-4 mx-4" style="width: 170px;">유저 검색</button></router-link>
        </div>
        <div class="d-flex row justify-content-center m-5">
          <div class="input-group mb-3">
            <input type="text" class="form-control fs-5" placeholder="유저 아이디" aria-label="Recipient's username" aria-describedby="button-addon2" required v-model="username" @keyup.enter="searchUsers">
            <button class="btn btn-outline-secondary fs-4" type="button" id="button-addon2" @click="searchUsers">search</button>
          </div>

          <div class="my-3" style="height: auto; width: 800px; background-color:#F4F3F3;" id="border">
            <div class="p-3">
              <table class="table table-borderless table-hover">
                <tbody v-if="userlist[0]">
                  <div v-for="user in userlist" :key="user.id">
                    <div class="border border-2 rounded-4 d-flex row m-2" style="background-color:white;" v-if="currentUser.username !== user.username">
                      <div class="d-flex justify-content-between pb-0">
                        <div>
                          <p class="fs-5 pt-2 mb-2">
                            {{ user.username }}
                          </p>
                        </div>
                        <div class="pt-1">
                          <a :href="'http://localhost:8080/home/'+user.username" class="text-decoration-none">
                            <img src="../assets/home.png" class="inline" style="width: 30px;">
                            <span style="color:black;"> 친구의 티미룸으로 이동</span>
                          </a>
                        </div>
                      </div>
                    </div>
                  </div>
                </tbody>
                <h5 v-else-if="!isSerched" class="pt-3 mb-0 text-center">친구를 검색해주세요!</h5>
                <h5 v-else class="pt-3 mb-0 text-center">찾으시는 친구가 없어요,,</h5>
              </table>
            </div>
          </div>
        </div>
      </div>

      <div class="ms-auto" style="height: 80vh; width: 0%;">
        <router-link :to="{ name: 'home', params: {username: currentUser.username} }" class="link_active"><button class="top-btn btn btn-light mb-2 rounded-end fs-4">홈</button></router-link>
        <router-link to="/movies/recommend" class="link"><button class="btn btn-light my-2 rounded-end fs-4">추천영화</button></router-link>
        <router-link :to="{ name: 'mymovie', params: {username: currentUser.username} }" class="link"><button class="btn btn-light my-2 rounded-end fs-4">내 영화</button></router-link>
        <router-link to="/movies/minigame" class="link"><button class="btn btn-light my-2 rounded-end fs-4">미니게임</button></router-link>
        <router-link to="/movies/friends" class="link"><button class="btn-light my-2 rounded-end fs-4">친구관리</button></router-link>
        <router-link to="/movies/settings" class="link"><button class="btn btn-light my-2 rounded-end fs-4">설정</button></router-link>  
      </div>

   </div>
  </div>
<!-- </div> -->

</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  data() {
    return {
      username: '',
      isSerched: false
    }
  },
  computed: {
    ...mapGetters(['profile', 'currentUser', 'followers', 'userlist'])
  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchCurrentUser', 'fetchFollowers', 'userList']),
    searchUsers() {
      this.userList(this.username)
      this.isSerched = true
    }
  },
  created() {
    this.fetchProfile(this.currentUser.username)
    this.fetchFollowers(this.currentUser.username)
    this.isSerched = false
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
 margin: 50px;
 margin-top: 100px;
}

.inline { 
  display: inline-block;
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

