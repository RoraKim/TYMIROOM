<template>
<div id="outer" v-if="this.profile.profile_set">
 <!-- <div class="home back d-flex justify-content-center align-items-center pb-5" style="background-color: #EA8D98;border:none;" id="border"> -->
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
            <img src="../assets/slate.png" style="width: 50px;"><h4 class="inline" style="margin: 10px;">인생영화</h4>
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
      
      <!-- 오른쪽 박스 -->
      <div style="height: 80vh; width: 75%; overflow:scroll;" class="p-5 m-2" id="border">
        <h1 class="fw-bold"> {{ this.$route.params.username }} 님의 티미룸</h1>
        <hr style="width: 900px">
        <!-- <h4 class="fw-bold">[티미룸]</h4>/ -->
        <div class="" style="height: 450px; width: 900px; position:relative; background-color:#F8F6F6;">
          <img :src="require('../assets/tymiroom/room'+ profile.profile_set[0].room_image + '.png')"
          style="height: 450px; width: 900px; padding-bottom: 0px" id="border">
          <img id="tymi-whole" :src="require('../assets/tymi_whole/tymi_'+ profile.profile_set[0].tymi_image + '.png')"
          style="position:absolute; left: 500px; top: 240px; height: 240px; width:auto;"
          >
        </div>
        <hr style="width: 900px">
        <h4 class="fw-bold">[방명록]</h4>
        <div class="my-3" style="height: auto; width: 900px; background-color:#F8F6F6;" id="border" v-if="this.profile.guestbook_me"> 
          <guestbook-list :guestbooks="profile.guestbook_me" v-if="profile.guestbook_me[0]"></guestbook-list>
          <h5 v-else class="p-3">방명록이 없어요,, 방명록을 남겨주세요!</h5>
        </div>
      </div>

      <div class="ms-auto" style="height: 80vh; width: 0%;">
        <router-link :to="{ name: 'home', params: {username: currentUser.username} }" class="link_active"><button class="top-btn btn-light mb-2 rounded-end fs-4">홈</button></router-link>
        <router-link to="/movies/recommend" class="link"><button class="btn btn-light my-2 rounded-end fs-4">추천영화</button></router-link>
        <router-link :to="{ name: 'mymovie', params: {username: currentUser.username} }" class="link"><button class="btn btn-light my-2 rounded-end fs-4">내 영화</button></router-link>
        <router-link to="/movies/minigame" class="link"><button class="btn btn-light my-2 rounded-end fs-4">미니게임</button></router-link>
        <router-link to="/movies/friends" class="link"><button class="btn btn-light my-2 rounded-end fs-4">친구관리</button></router-link>
        <router-link to="/movies/settings" class="link"><button class="btn btn-light my-2 rounded-end fs-4">설정</button></router-link>    
      </div>
    </div>

    <!-- 친구일 경우 -->

    <div class="d-flex p-2" style="height: 84vh; width: 74%; background-color: #a2d2ff;" id="inner" v-else>

      <div class="d-flex p-5 m-2" style="height: 80vh; width: 25%; background-color:#dceef3;" id="border">
      <div class = "d-flex justify-content-center row">
        <!-- 티미 사진 -->
        <div class="border cards" style="height:250px; width: 250px; background-color:#FCFEFF; padding:0; box-shadow:none;">
          <img :src="require('../assets/tymi_profile/'+ profile.profile_set[0].tymi_image + '_profile.png')" style="height:250px; width: 250px;">
        </div>
        
        <div class="sub d-flex justify-content-center" v-if="this.followers.followings">
          <img src="../assets/button/unfol.png" style="width:180px; height:70px;" id="buttons" @click="clickFollow()" v-if="isFollowed">
          <img src="../assets/button/fol.png" style="width:180px; height:70px;" id="buttons" class="me-4" @click="clickFollow()" v-else>
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





        <!-- 친구 파도타기 -->
        <select class="form-select form-select mb-3 fs-4" style="height: 50px;" onchange="location.href=(value);">
          <option selected value="none">친구 파도타기</option>
          <option v-for="friend in this.followers.followers" :key="friend.id" :value="'http://localhost:8080/home/'+friend.username">{{ friend.username }}</option>
        </select>
      </div>
    </div>
      
      <div style="height: 80vh; width: 75%; overflow:scroll;" class="p-5 m-2" id="border">
        <h1> {{ this.$route.params.username }} 님의 티미룸</h1>
        <hr style="width: 900px">
        <!-- <h4 class="fw-bold">[티미룸]</h4>/ -->
        <div class="" style="height: 450px; width: 900px; position:relative; background-color:#F8F6F6;">
          <img :src="require('../assets/tymiroom/room'+ profile.profile_set[0].room_image + '.png')"
          style="height: 450px; width: 900px; padding-bottom: 0px" id="border">
          <img id="tymi-whole" :src="require('../assets/tymi_whole/tymi_'+ profile.profile_set[0].tymi_image + '.png')"
          style="position:absolute; left: 500px; top: 240px; height: 240px; width:auto;"
          >
        </div>
        <hr style="width: 900px">
        <h4 class="fw-bold">[방명록]</h4>
        <div v-if="this.followers.followings">
          <div class="my-3" style="height: auto; width: 900px; background-color:#F8F6F6;" id="border" v-if="isFollowed"> 
            <guestbook-list :guestbooks="profile.guestbook_me"></guestbook-list>
          </div>
          <div class="my-3" style="height: auto; width: 900px; background-color:#F8F6F6;" id="border" v-else>
            <h4 class="pt-3 text-center" style="height:60px;">친구를 팔로우하고 방명록을 남겨보세요!</h4>
          </div>
        </div>
      </div>

      <div class="ms-auto" style="height: 80vh; width: 0%;" v-if="this.followers.followings">
      <router-link :to="{ name: 'home', params: {username: this.$route.params.username} }" class="link"><button class="top-btn btn btn-light mb-2 f-rounded-end fs-4" style="background-color:white;">홈</button></router-link>
      <router-link :to="{ name: 'mymovie', params: {username: this.$route.params.username} }" class="link"><button class="btn btn-light my-2 f-rounded-end fs-5">친구의영화</button></router-link>
      </div>
    </div>
  </div>
<!-- </div> -->

</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import Swal from 'sweetalert2'

import GuestbookList from '@/components/GuestbookList.vue'

export default {
  name: 'ProfileView',
  components:{
    GuestbookList,
  },
  computed: {
    ...mapGetters(['profile', 'currentUser', 'followers']),
    isFollowed() {
      const currentUser = this.currentUser
      return this.followers.followings.some(function (user) {
        return user['id'] === currentUser.pk
      })
    }
  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchCurrentUser', 'follow', 'fetchFollowers']),
    clickFollow() {
      if(this.isFollowed) {
        this.follow(this.$route.params.username)
        Swal.fire(`${this.$route.params.username}님 팔로우를 취소하였습니다.`)
        this.fetchFollowers(this.$route.params.username)
      }
      else{
        this.follow(this.$route.params.username)
        Swal.fire(`${this.$route.params.username}님을 팔로우 하였습니다.`)
        this.fetchFollowers(this.$route.params.username)
      }
    }
  },
  created() {
    this.fetchCurrentUser(),
    this.fetchFollowers(this.$route.params.username),
    this.fetchProfile(this.$route.params.username)
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
.cards {
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}

#border { 
/* box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25); */
border-radius: 10px;
background-color: white;
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

.inline { 
  display: inline-block;
}
#tymi-whole:hover {
  animation: motion 0.3s linear 0s infinite alternate; 
  margin-top: 0px;
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

@keyframes motion {
  from {transform: translate3d(0, 0, 0);}
  to {transform: translate3d(0, -15px, 0);}
}

#buttons:hover {
  cursor: pointer;
}
</style>






