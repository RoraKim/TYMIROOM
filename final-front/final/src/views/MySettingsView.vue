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
      
      <!-- 오른쪽 박스 -->
      <div style="height: 80vh; width: 75%; overflow:scroll;" class="p-5 m-2" id="border">
        <h1 class="fw-bold">설정</h1>
        <div class="d-flex justify-content-center">
          <router-link to="/movies/settings" class="link"><button class="btn btn-outline-secondarys fs-4 mx-4" style="width: 170px;">티미룸 꾸미기</button></router-link>
          <router-link to="/movies/settings/profile" class="link"><button class="btn btn-outline-secondarys fs-4 mx-4" style="width: 170px; background-color:#F5D6CB;">내 계정 관리</button></router-link>
        </div>
        <div class="m-4">
          <div class="d-flex justify-content-center">
            <div style="width: 800px; background-color:#fff1f1;" id="border" class="p-3">
              <div class="">
                <h3 v-if="this.profile.profile_set[0].level === 0" class="mt-2 mb-3">
                  레벨 업 하시면 더 많은 티미와 티미룸을 설정할 수 있어요!
                  </h3>
                <h4 class="fw-bold">[티미]</h4>
                  <div>
                    <input type="radio" id="pink" name="tymi" value="pink" v-model="tymi" checked>
                    <label for="pink"><img src="../assets/tymi_profile/pink_profile.png" style="height:150px; width:auto;" class="px-2"><span class="fs-3">PINK TYMI</span></label><br>
                  </div>
                  <div>
                    <input type="radio" id="skyblue" name="tymi" value="skyblue" v-model="tymi">
                    <label for="skyblue"><img src="../assets/tymi_profile/skyblue_profile.png" style="height:150px; width:auto;" class="px-2"><span class="fs-3">SKYBLUE TYMI</span></label><br>
                  </div>
                  <div>
                    <input type="radio" id="red" name="tymi" value="red" v-model="tymi">
                    <label for="red"><img src="../assets/tymi_profile/red_profile.png" style="height:150px; width:auto;" class="px-2"><span class="fs-3">RED TYMI</span></label><br>
                  </div>
                  <div v-if="this.profile.profile_set[0].level === 1">
                    <input type="radio" id="blue" name="tymi" value="blue" v-model="tymi">
                    <label for="blue"><img src="../assets/tymi_profile/blue_profile.png" style="height:150px; width:auto;" class="px-2"><span class="fs-3">BLUE TYMI</span></label><br>
                  </div>
                  <div v-if="this.profile.profile_set[0].level === 1">
                    <input type="radio" id="purple" name="tymi" value="purple" v-model="tymi">
                    <label for="purple"><img src="../assets/tymi_profile/purple_profile.png" style="height:150px; width:auto;" class="px-2"><span class="fs-3">PURPLE TYMI</span></label><br>
                  </div>
                  <div v-if="this.profile.profile_set[0].level === 1">
                    <input type="radio" id="green" name="tymi" value="green" v-model="tymi">
                    <label for="green"><img src="../assets/tymi_profile/green_profile.png" style="height:150px; width:auto;" class="px-2"><span class="fs-3">GREEN TYMI</span></label><br>
                  </div>
                  <div v-if="this.profile.profile_set[0].level === 1">
                    <input type="radio" id="violet" name="tymi" value="violet" v-model="tymi">
                    <label for="violet"><img src="../assets/tymi_profile/violet_profile.png" style="height:150px; width:auto;" class="px-2"><span class="fs-3">VIOLET TYMI</span></label><br>
                  </div> <hr>
                <h4 class="fw-bold">[티미룸]</h4>
                  <div>
                    <input type="radio" id="1" name="room" value="1" v-model="room" checked>
                    <label for="1"><img src="../assets/tymiroom/room1.png" style="height:150px; width:300px;" class="px-4"><span class="fs-4">ROOM 1</span></label><br>
                  </div>
                  <div>
                    <input type="radio" id="3" name="room" value="3" v-model="room">
                    <label for="3"><img src="../assets/tymiroom/room3.png" style="height:150px; width:300px;" class="px-4"><span class="fs-4">ROOM 2</span></label><br>
                  </div>
                  <div>
                    <input type="radio" id="4" name="room" value="4" v-model="room">
                    <label for="4"><img src="../assets/tymiroom/room4.png" style="height:150px; width:300px;" class="px-4"><span class="fs-4">ROOM 3</span></label><br>
                  </div>
                  <div v-if="this.profile.profile_set[0].level === 1">
                    <input type="radio" id="5" name="room" value="5" v-model="room">
                    <label for="5"><img src="../assets/tymiroom/room5.png" style="height:150px; width:300px;" class="px-4"><span class="fs-4">ROOM 4</span></label><br>
                  </div>
                  <div v-if="this.profile.profile_set[0].level === 1">
                    <input type="radio" id="6" name="room" value="6" v-model="room">
                    <label for="6"><img src="../assets/tymiroom/room6.png" style="height:150px; width:300px;" class="px-4"><span class="fs-4">ROOM 5</span></label><br>
                  </div>
                  <div v-if="this.profile.profile_set[0].level === 1">
                    <input type="radio" id="7" name="room" value="7" v-model="room">
                    <label for="7"><img src="../assets/tymiroom/room7.png" style="height:150px; width:300px;" class="px-4"><span class="fs-4">ROOM 6</span></label><br>
                  </div>
                <div class="text-center">
                  <button class="m-2 btn rounded-end fs-3" style="width:150px; height:50px;" @click="updateTymiProfile">바꾸기</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="ms-auto" style="height: 80vh; width: 0%;">
        <router-link :to="{ name: 'home', params: {username: currentUser.username} }" class="link_active"><button class="top-btn btn btn-light mb-2 rounded-end fs-4">홈</button></router-link>
        <router-link to="/movies/recommend" class="link"><button class="btn btn-light my-2 rounded-end fs-4">추천영화</button></router-link>
        <router-link :to="{ name: 'mymovie', params: {username: currentUser.username} }" class="link"><button class="btn btn-light my-2 rounded-end fs-4">내 영화</button></router-link>
        <router-link to="/movies/minigame" class="link"><button class="btn btn-light my-2 rounded-end fs-4">미니게임</button></router-link>
        <router-link to="/movies/friends" class="link"><button class="btn btn-light my-2 rounded-end fs-4">친구관리</button></router-link>
        <router-link to="/movies/settings" class="link"><button class="btn-light my-2 rounded-end fs-4">설정</button></router-link>    
      </div>

   </div>
  </div>
<!-- </div> -->

</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import Swal from 'sweetalert2'


export default {
  name: 'ProfileView',
  data() {
    return{
      tymi: 'pink',
      room: '1',
    }
  },
  computed: {
    ...mapGetters(['profile', 'currentUser'])
  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchCurrentUser', 'updateProfile']),
    updateTymiProfile() {
      this.updateProfile({ tymi: this.tymi, room: this.room, user: this.currentUser.pk })
      Swal.fire('티미룸이 업데이트 되었습니다!')
      this.$router.push({ name: 'home', params: {username: this.currentUser.username} })
      
    }
  },
  created() {
    this.fetchProfile(this.currentUser.username)
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

