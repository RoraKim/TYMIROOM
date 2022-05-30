<template>
<div id="outer">
 <!-- <div class="home back d-flex justify-content-center align-items-center pb-5"> -->
  <div class="d-flex p-2" style="height: 84vh; width: 74%; background-color:#EA8D98;" id="inner">
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
    <!-- 오른쪽 메인 박스 -->
    <div style="height: 80vh; width: 75%; overflow:scroll; background-color: white;" class="p-5 m-2 pb-0" id="border">
      <div v-if="question === 1">
        <h1 class="fw-bold">배우 월드컵</h1>
        <hr style="width: 900px">
      <div class="d-flex row justify-content-center allgin-items-center mb-2">
        <div style="margin-left:500px; margin-top: 50px" class="">
          <h2 style="margin-left: 25px">내가 더 관심있는 배우를 찾아서</h2>
          <h2 class="">그들의 작품을 추천 받을 수 있어요!</h2>
        </div>
          <img src="../assets/lalaland.jpg" class="gameimg my-5" alt="" style="display: block">
          <h1 style="margin-left:770px;">round : 16</h1>
        <!-- <button class="btn fs-1" style="height: 90px; width: 400px; margin-top:20px;">16강 시작하기</button> -->
      <img src="../assets/start.png" class="" @click="onClickButton()" alt="" style="width: 200px; cursor: pointer;">
         
      </div>
      
    </div>
    <div class="worldcup">

    <!-- 게임중 -->
    <div v-if="question === 2">
    <div v-if="!finishFlag">
      <h1>더 좋아하는 배우를 선택해 주세요</h1>
      <hr>
      <div v-if="!left">
        <div class="d-flex row justify-content-center" style="">
          <h1 style="margin-left:550px; margin-top: 100px">다음 라운드로 달려볼까요?</h1>
          <h2 style="margin-left:815px; margin-top:50px; margin-bottom:50px;">round : {{ roundNum }}</h2>
        <!-- <button class="btn fs-1" style="height: 90px; width: 400px; margin-top:20px;">16강 시작하기</button> -->
          <img src="../assets/start.png" class="" @click="next" alt="" style="width: 200px; cursor: pointer;">
          <!-- <button @click="next" class="btn fs-1" style="height: 90px; width: 400px; margin-top:180px;">{{ roundNum }}강 시작하기</button> -->
        </div>
      </div>
      <div class="d-flex justify-content-between">
        <div class="mt-3 mx-5 select-body">
          <br>
          <br>
          <actor-game-detail id="left" :actor="left" @choiceEvent="leftChoice"></actor-game-detail>
        </div>
        <div v-if="left">
        <img src="../assets/vs1.png" alt="" style="width:70px; height: 70px; margin-top:300px">
        </div>
        <div class="mt-3 mx-5 select-body">
          <br>
          <br>
          <actor-game-detail id="right" :actor="right" @choiceEvent="rightChoice"></actor-game-detail>
        </div>
      </div>
    </div>

    <!-- 게임 끝 -->
    <div v-if="finishFlag && left.actor_id">
      <!-- <p class="text-center fs-4 m-0">배우 이상형 월드컵 우승</p> -->
      <h1 class="text-center">{{ left.name }}를 선택하셨군요!</h1>
      <br>
      <h3 class="text-center"> 배우를 눌러 출연작을 알아보세요!</h3>
      <br>
      <h2></h2>
      <div class="d-flex justify-content-center">
        <div class="d-flex row justify-content-center">
          <div class="card shadow" style="width:auto;">
            <img :src="'https://image.tmdb.org/t/p/original/' + left.profile_path" class="card-img-top p-2 mb-1" alt="..." style="height: 500px; width:300px;">
            <a href="" class="stretched-link" data-bs-toggle="modal" :data-bs-target="'#staticBackdrop' + left.actor_id" @click="fetchActor(left.actor_id)"></a>
            <div class="d-flex justify-content-center mb-3">
              <br>
              <br>
              <!-- <button class="btn fs-4" style="height: 45px; width: 180px;" data-bs-toggle="modal" :data-bs-target="'#staticBackdrop' + left.actor_id" @click="fetchActor(left.actor_id)">배우 추천 영화</button> -->
            </div>
          </div>
          <router-link to="/movies/minigame" class="link_active text-center"><img src="../assets/back.png" class="inline" style="width: 200px; margin-top:20px; margin-bottom:0px; margin-left: 20px; cursor: pointer;">
            <!-- <h4 class="inline" style="color: black; margin: 10px">미니게임 홈으로</h4> -->
          </router-link>
        </div>
      </div>
    </div>
    <div v-if="left">
      <div class="modal fade" :id="'staticBackdrop' + left.actor_id" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable modal-xl">
          <div class="modal-content">
            <div class="modal-body p-4" >
              <actor-detail :actorId="left.actor_id"></actor-detail>
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


    </div>
    <!-- 오른쪽 메인 박스 종료 -->
    <!-- 사이드 버튼 -->
    <div class="ms-auto" style="height: 80vh; width: 0%;">
      <router-link :to="{ name: 'home', params: {username: currentUser.username} }" class="link_active"><button class="top-btn btn btn-light mb-2 rounded-end fs-4">홈</button></router-link>
      <router-link to="/movies/recommend" class="link"><button class="btn btn-light my-2 rounded-end fs-4">추천영화</button></router-link>
      <router-link :to="{ name: 'mymovie', params: {username: currentUser.username} }" class="link"><button class="btn btn-light my-2 rounded-end fs-4">내 영화</button></router-link>
      <router-link to="/movies/minigame" class="link"><button class="btn-light my-2 rounded-end fs-4">미니게임</button></router-link>
      <router-link to="/movies/friends" class="link"><button class="btn btn-light my-2 rounded-end fs-4">친구관리</button></router-link>
      <router-link to="/movies/settings" class="link"><button class="btn btn-light my-2 rounded-end fs-4">설정</button></router-link>    
    </div>
    <!-- 사이드 버튼 종료 -->
  </div>
</div>

</template>

<script>
import { mapGetters, mapActions} from 'vuex'
import ActorGameDetail from '@/components/ActorGameDetail.vue'
import ActorDetail from '@/components/ActorDetail.vue'

export default {
  name: 'ActorGameView',

  data () {
    return {
      current_round: [],
      next_round: [],
      roundNum: 16,
      left: null,
      right: null,
      finishFlag: false,
      question: 1
    }
  },

  components: { ActorGameDetail, ActorDetail },
  computed: {
    ...mapGetters(['currentUser', 'movies','actors', 'recommendation', 'profile'])
  },
  methods: {
    ...mapActions(['fetchActorGames', 'fetchMovie', 'wishMovie', 'seenMovie', 'updateProfile', 'fetchProfile', 'fetchActor']),


     randomActorCall(){
      for(let i in this.actors){
          this.current_round.push(this.actors[i])
          console.log(this.actors[i])
          console.log(this.current_round)
        
      }
      this.next()
    },

    leftChoice() {
      this.next_round.push(this.left)
      this.left = null
      this.right = null
      this.next()
    },

    rightChoice() {
      this.next_round.push(this.right)
      this.left = null
      this.right = null
      this.next()
    },

    next() {
      this.left = this.current_round.pop()
      this.right = this.current_round.pop()
    },   
    onClickButton() {
      this.question ++;
      },
  },

  watch: {
    //라운드 종료 판별
    left: function() {
      if (this.current_round.length === 0 && !this.left) {
        this.current_round = this.next_round
        this.next_round = []
        this.roundNum = this.current_round.length
      }
    },
    //우승자 판별
    right: function() {
      if (this.next_round.length === 0 && this.current_round.length === 1 && !this.left && !this.right) {
        this.left = this.current_round.pop()
        this.finishFlag = true
        console.log(this.left)
        // .then(res=>{
        //   console.log(res)
        // })
      }
    }
  },

  created() {
    // this.fetchCurrentUser()
    // this.fetchActorGames(),
    this.randomActorCall()
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

.inline { 
  display: inline-block;
}

.select-body:hover {
  transition: all 0.3s ease-in-out; 
  transform: scale(1.1);
  -webkit-transform: scale(1.1);
  -moz-transform: scale(1.1);
  -ms-transform: scale(1.1);
  -o-transform: scale(1.1);
}

.gameimg {
  width: 300px;
  height: 300px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
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
/* .sub { 
  margin-bottom: 1px;
  padding: 5px;
} */
</style>
