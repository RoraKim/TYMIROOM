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
          <router-link to="/movies/settings" class="link"><button class="btn btn-outline-secondarys fs-4 mx-4" style="width: 170px; background-color:#F5D6CB;">티미룸 꾸미기</button></router-link>
          <router-link to="/movies/settings/profile" class="link"><button class="btn btn-outline-secondarys fs-4 mx-4" style="width: 170px;">내 계정 관리</button></router-link>
        </div>
        <div class="m-4">
          <div class="d-flex justify-content-center">
            <div style="width: 800px; background-color:#fff1f1;" id="border" class="p-3">
              <h4 class="fw-bold py-3">[비밀번호 변경]</h4>
              <account-error-list v-if="authError"></account-error-list>
              <form @submit.prevent="submitPassword">
                <div>
                  <label for="password1">비밀번호</label><br>
                  <input v-model="credentials.new_password1" type="password" id="password1" required style="" placeholder="비밀번호를 입력하세요" class="p-3 fs-5 mt-0"/>
                </div>
                <div>
                  <label for="password2" style="margin-right:10px">비밀번호 확인</label><br>
                  <input v-model="credentials.new_password2" type="password" id="password2" required style="" placeholder="비밀번호를 한번 더 입력하세요" class="p-3 fs-5 mt-0"/>
                </div>
                <div>
                  <button id="submit-button">제출</button>
                </div>
              </form>
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
import AccountErrorList from '@/components/AccountsErrorList.vue'

export default {
  name: 'ProfileView',
  components: {
    AccountErrorList
  },
  data() {
    return{
      credentials: {
        new_password1: '',
        new_password2: ''
      }
    }
  },
  computed: {
    ...mapGetters(['profile', 'currentUser', 'authError'])
  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchCurrentUser', 'updateProfile', 'passwordChange']),
    updateTymiProfile() {
      this.updateProfile({ tymi: this.tymi, room: this.room, user: this.currentUser.pk })
    },
    submitPassword() {
      this.passwordChange(this.credentials)
      this.credentials.new_password1 = ''
      this.credentials.new_password2 = ''
      Swal.fire({
        icon: 'success',
        title: '비밀번호가 변경되었습니다!',
      })

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

label{
  font-size: 1.5rem;
  display:inline;
}

#submit-button { 
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
  height: 40px; width: 135px;
  border: #EA8D98;
  background: #FCFEFF;
  border-radius: 10px;
  margin: 30px;
  font-size: 20px;
  
}

input {
  /* position: absolute; */
width: 280px;
height: 40px;
left: 537px;
top: 258px;
margin-top:25px;
margin-bottom: 20px;

/* #FCFEFF/white */

background: #FCFEFF;
box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
border-radius: 10px;
border: #FCFEFF;
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

