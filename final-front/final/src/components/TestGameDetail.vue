<template>
  <div>
    <div class="d-flex justify-content-center row" style="padding: 30px">
      
      <div v-if="question === 0">
        <div class="d-flex row justify-content-center align-items-center mb-2">
          <div style="margin-left:500px; margin-top: 50px" class="">
            <h2 style="margin-left: 50px">심리 테스트를 통해</h2>
            <br>
            <h2 class="">내가 좋아하는 장르를 찾아봐요!</h2>
          </div>
          <img src="../assets/lalaland.jpg" class="gameimg my-5" alt="" style="display: block">
          <h1 style="margin-left:770px;"></h1>
          <img src="../assets/start.png" class="" @click="next()" alt="" style="width: 200px; cursor: pointer;"> 
        </div>
      </div>

      <!-- 1번 질문 -->
      <div v-if="question === 1" style="" class="d-flex row p-4">
      <!-- 프로그래스 바 -->
        <div class="progress" style="height: 8px; background: #C4C4C4; width: 100%; margin-top:40px; padding:0px" >
          <div class="progress-bar" role="progressbar" style="width: 0%; background: #EA8D98;" aria-valuenow="8.333333333333332" aria-valuemin="0" aria-valuemax="100"></div>
        </div> 
        <h1 style="margin-top:40px">Q.1</h1>
        <h3 style="height: 70px;">유튜브에 들어간 당신, 어떤 영상을 선택할 건가요?</h3>
        <button @click="onClickButton(35)" style="display:block" class="answer-box answer-font mt-3 mb-2" >
          <p class="m-0">
            배꼽 잡는 웃긴 영상
          </p>
        </button>
        <br>

          <button @click="onClickButton(28)" class="answer-box answer-font mt-3 mb-2">
            <p class="m-0">
              뿌슝 뿌슝 화려한 액션
            </p>
          </button>
          <div>
            <br>
          </div>

          <button @click="onClickButton(99)" class="answer-box answer-font mt-3 mb-2">
            <p class="m-0">
              근엄 진지 뉴스 혹은 다큐멘터리
            </p>
          </button>


          <button @click="onClickButton(18)" class="answer-box answer-font mt-3 mb-2">
            <p class="m-0">
              로맨틱한 드라마 
            </p>
          </button>
        </div>

<!-- 2번 질문 -->
      <div v-if="question === 2" class="d-flex row p-4">
      <!-- 프로그래스 바 -->
    <div class="progress" style="height: 8px; background: #C4C4C4; width: 100%; margin-top:40px; padding:0px">
    <div class="progress-bar" role="progressbar" style="width: 12.5%; background: #EA8D98;" aria-valuenow="8.333333333333332" aria-valuemin="0" aria-valuemax="100"></div>
  </div> 

  
  <h1 style="margin-top:40px">Q.2</h1>
  <h3 style="height: 70px;">인생에서 가장 중요한건 무엇인가요?</h3>
  <button @click="onClickButton(10749)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        인생은 사랑이지
      </p>
    </button>
    <br>

    <button @click="onClickButton(12)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        인생은 도전이지
      </p>
    </button>
    <div>
      <br>
    </div>

    <button @click="onClickButton(35)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        재미 없으면 사나마나
      </p>
    </button>

    <button @click="onClickButton(10751)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        평화롭게 살다 가는게 제일이다
      </p>
    </button>
  </div>

  <!-- 3번 질문 -->
      <div v-if="question === 3" class="d-flex row p-4">
      <!-- 프로그래스 바 -->
    <div class="progress" style="height: 8px; background: #C4C4C4; width: 100%;  margin-top:40px; padding:0px" >
    <div class="progress-bar" role="progressbar" style="width: 25%; background: #EA8D98;" aria-valuenow="8.333333333333332" aria-valuemin="0" aria-valuemax="100"></div>
  </div> 

  
  <h1 style="margin-top:40px">Q.3</h1>
  <h3 style="height: 70px;">회사에 들어간 당신, 어떤 유형의 직장 동료가 그나마 가장 낫나요?</h3>
  <button @click="onClickButton(53)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        지나치게 원칙대로 하는 부장님
      </p>
    </button>
    <br>

    <button @click="onClickButton(10749)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        시도때도 없이 추근덕 대는 동기
      </p>
    </button>
    <div>
      <br>
    </div>

    <button @click="onClickButton(99)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        농담도 안받아주는 진지한 사수
      </p>
    </button>

    <button @click="onClickButton(18)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        매사에 해맑은 후배
      </p>
    </button>
  </div>

  <!-- 4번 질문 -->
      <div v-if="question === 4" class="d-flex row p-4">
      <!-- 프로그래스 바 -->
    <div class="progress" style="height: 8px; background: #C4C4C4; width: 100%; margin-top:40px; padding:0px">
    <div class="progress-bar" role="progressbar" style="width: 37.5%; background: #EA8D98;" aria-valuenow="8.333333333333332" aria-valuemin="0" aria-valuemax="100"></div>
  </div> 

  
  <h1 style="margin-top:40px">Q.4</h1>
  <h3 style="height: 70px;">여행지를 선택할 수 있다면 어디를 선택할 건가요?</h3>
  <button @click="onClickButton(10751)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        집
      </p>
    </button>

    <button @click="onClickButton(28)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        화려한 도시
      </p>
    </button>

    <button @click="onClickButton(12)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        나만 아는 관광지
      </p>
    </button>

    <button @click="onClickButton(53)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        귀곡산장
      </p>
    </button>
  </div>

    <!-- 5번 질문 -->
      <div v-if="question === 5" class="d-flex row p-4">
      <!-- 프로그래스 바 -->
    <div class="progress" style="height: 8px; background: #C4C4C4; width: 100%; margin-top:40px; padding:0px">
    <div class="progress-bar" role="progressbar" style="width: 50%; background: #EA8D98;" aria-valuenow="8.333333333333332" aria-valuemin="0" aria-valuemax="100"></div>
  </div> 

  
  <h1 style="margin-top:40px">Q.5</h1>
  <h3 style="height: 70px;">이벤트에 당첨되어 무료 티켓을 받은 당신, 누구에게 같이 가자고 할 건가요?</h3>
  <button @click="onClickButton(10751)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        가족
      </p>
    </button>

    <button @click="onClickButton(28)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        친구들
      </p>
    </button>

    <button @click="onClickButton(10749)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        연인
      </p>
    </button>

    <button @click="onClickButton(99)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        나 혼자
      </p>
    </button>
  </div>

      <!-- 6번 질문 -->
      <div v-if="question === 6" class="d-flex row p-4">
      <!-- 프로그래스 바 -->
    <div class="progress" style="height: 8px; background: #C4C4C4; width: 100%; margin-top:40px; padding:0px">
    <div class="progress-bar" role="progressbar" style="width: 62.5%; background: #EA8D98;" aria-valuenow="8.333333333333332" aria-valuemin="0" aria-valuemax="100"></div>
  </div> 

    <h1 style="margin-top:40px">Q.6</h1>
  <h3 style="height: 70px;">다음 중 가장 오글거리는 장면은 무엇인가요?</h3>
  <button @click="onClickButton(12)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        하이틴 영화의 한 장면
      </p>
    </button>

    <button @click="onClickButton(99)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        주인공과 가족이 눈물의 재회를 하는 장면
      </p>
    </button>

    <button @click="onClickButton(53)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        주인공이 역경을 이겨내고 뿌듯한 표정으로 화면을 응시하는 장면
      </p>
    </button>

    <button @click="onClickButton(35)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        연인이 서로에게 진한 애정표현을 하는 장면
      </p>
    </button>
  </div>

 <!-- 7번 질문 -->
      <div v-if="question === 7" class="d-flex row p-4">
      <!-- 프로그래스 바 -->
    <div class="progress" style="height: 8px; background: #C4C4C4; width: 100%; margin-top:40px; padding:0px" >
    <div class="progress-bar" role="progressbar" style="width: 75%; background: #EA8D98;" aria-valuenow="8.333333333333332" aria-valuemin="0" aria-valuemax="100"></div>
  </div> 

    <h1 style="margin-top:40px">Q.7</h1>
  <h3 style="height: 70px;">당신이 싫어하는 사람이 당신의 험담을 했다는 걸 알게 되었다. 당신의 행동은?</h3>
  <button @click="onClickButton(35)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        어쩔 수 없지… 나도 그 사람 욕 하는걸? 쿨하게 넘긴다
      </p>
    </button>

    <button @click="onClickButton(53)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        앞에서는 쿨한 척 하지만 복수를 계획한다
      </p>
    </button>

    <button @click="onClickButton(18)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        가족, 친구들에게 상담한다
      </p>
    </button>

    <button @click="onClickButton(28)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        당장 찾아가서 따진다
      </p>
    </button>
  </div>


 <!-- 8번 질문 -->
      <div v-if="question === 8" class="d-flex row p-4">
      <!-- 프로그래스 바 -->
    <div class="progress" style="height: 8px; background: #C4C4C4; width: 100%; margin-top:40px; padding:0px" >
    <div class="progress-bar" role="progressbar" style="width: 87.5%; background: #EA8D98;" aria-valuenow="8.333333333333332" aria-valuemin="0" aria-valuemax="100"></div>
  </div> 

    <h1 style="margin-top:40px">Q.8</h1>
  <h3 style="height: 70px;">놀이공원에 간 당신, 어떤 놀이기구를 가장 좋아하나요?</h3>
  <button @click="onClickButton(35)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        귀신의 집
      </p>
    </button>

    <button @click="onClickButton(53)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        롤러코스터
      </p>
    </button>

    <button @click="onClickButton(18)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        관람차
      </p>
    </button>

    <button @click="onClickButton(28)" class="answer-box answer-font mt-3 mb-2">
      <p class="m-0">
        회전목마
      </p>
    </button>
  </div>



<div v-if="question === 9">
  <!-- result에서 가장 많이 나온 장르를 찾아서  -->
  <!-- 당신에게 어울리는 장르는 코미디입니다 -->
  <!-- 코미디 영화 추천받으러가기 -->

  <div class="d-flex row justify-content-center">
    <h2 style="margin-left: 125px; margin-top: 50px; margin-bottom: 50px;">
      티미가 취향을 열심히 분석 중이에요!
    </h2>
  <img src="../assets/clock.png" style="width: 300px; margin-bottom: 50px;">
  <div><br></div>
  
  <img src="../assets/go.png" class="" @click="resultMovies()" alt="" style="width: 150px; margin-bottom: 50px; cursor: pointer;"> 
</div>
</div>

  <!-- 결과 화면 -->
  <div v-if="question === 10">
    <h3 style="margin-bottom: 20px;">심리테스트 결과...</h3>
    <h3 class="d-inline">당신을 위한 추천 장르는 "</h3><h2 class="fw-bold d-inline">{{ movies.name }}</h2><h3 class="d-inline">"입니다</h3>

    <!-- 추천 영화 목록 -->
      <div class="row row-cols-1 row-cols-md-3 g-4 mt-3" v-if="movies.genre_movies">
        <div class="col" v-for="movie in movies.genre_movies.slice(0, 21)" :key="movie.id">
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
                  <div class="modal-body p-4" >
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

    <!-- 미니게임으로 돌아가기 -->
    <router-link to="/movies/minigame" class="link"><button class="btn btn-primary my-2 rounded-end" style="height: 40px; width: 90px;">미니게임 돌아가기</button></router-link>
  </div>
    




  </div>
  </div>
</template>

<script>
import { mapGetters, mapActions} from 'vuex'
import MovieDetail from '@/components/MovieDetail.vue'

export default {
  data() { 
    return{
      question : 0,
      // result : {genre:0}
      result : {35: 0, 28: 0, 99: 0, 18:0, 10749:0, 12:0, 10751:0, 53:0},
      
      
    }
    
  },
  components: { MovieDetail },

  computed: { 
    ...mapGetters(['currentUser', 'movies'])
  },

  methods: {
    ...mapActions(['fetchGenreMovies', 'fetchMovie', 'fetchRecommendation']),

    onClickButton(genre) {
    this.question ++;

    this.result[genre] ++
    },

    next(){
      this.question ++;
    },

    resultMovies() {
    this.question ++;
    // result에 담긴 값 중 가장 많이 나온 값 찾기 
    // 그걸 어딘가에 담아서 넘겨주기 
    let num = 0
    let genre_key = 0
    for( let i in this.result ){
      console.log(num)
      if (num < this.result[i]){
        num = this.result[i]
        genre_key = i
      }
      // console.log(genre_key)}
    
    // 가장 큰 value
    // console.log(num)
    this.fetchGenreMovies(genre_key)
    }},
    
  }
}

</script>

<style>

.answer-box { 
  width: 400px;
  height: 100px;
  margin-left: 10px;  
  border-radius: 10px;
  font-size: 30px;
  background-color: #FFEBEF;
  /* border-color: ; */
  border: solid #FFB7C5 5px;

}

.gameimg {
  width: 300px;
  height: 300px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}
</style>
