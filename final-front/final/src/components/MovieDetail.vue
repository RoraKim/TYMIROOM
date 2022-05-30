<template>
  <div>
    <div class="d-flex justify-content-between">
      <div>
      <h1 class="fw-bold" id="title">{{ movie.title }}</h1>
        <span v-for="(genre, index) in movie.genres" :key="index" id="genres" class="mx-1 fs-4">{{ genre.name }}</span>
      </div>
      <div>
        <img src="../assets/button/del.png" style="width:180px; height:auto;" id="buttons" class="mt-2" @click="addWishList(movieId)" v-if="isWished">
        <img src="../assets/button/add.png" style="width:180px; height:auto;" id="buttons" class="mt-2" @click="addWishList(movieId)" v-else>

      </div>
    </div>
    <hr>
    <div class="d-flex">
      <div class="d-flex row justify-content-center">
        <div class="d-flex row justify-content-center mb-5" style="width:auto; height:70px;">
          <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" style="height: 500px; width:auto;">
          <img src="../assets/button/my.png" style="width:230px; height:auto;" id="buttons" class="mt-4" @click="onClickProfileUpdate()">
        </div>
      </div>
      <div class="mx-5" style="width: 70%;">
        <h4 class="fw-bold">[줄거리]</h4>
        <p class="fs-4">{{ movie.overview }}</p>
        <h4 class="fw-bold">[출연진]</h4>
        <carousel
        v-if="movie.actors.length"
        :perPage="4"
        :navigationEnabled="true"
        :paginationPadding="5"
        :speed="300"
        >
          <slide v-for="actor in movie.actors" :key="actor.id">
            <div class="card d-flex justify-content-center mx-2">
              <img :src="'https://image.tmdb.org/t/p/original/' + actor.profile_path" 
              v-if="actor.profile_path"
              class="card-img">
              <img src="../assets/no_profile.png" alt="" v-else class="card-img">
              <p class="text-center">{{ actor.name }}</p>
            </div>
          </slide>
        </carousel>
      </div>
    </div><hr>
    <div>
      <h4 class="fw-bold">[추천영화]</h4>
       <carousel 
        v-if="recommendation.results.length"
        :perPage="6"
        :paginationPadding="0"
        :speed="300"
        class="active my-4">
          <slide v-for="recommendationMovie in recommendation.results" :key="recommendationMovie.id" class="active">
            <div class="card d-flex justify-content-center mx-2">
              <img :src="'https://image.tmdb.org/t/p/original/' + recommendationMovie.poster_path" class="card-img p-2 pb-3" style="height:250px;">
              <div class="card-body" style="margin-top: 0;">
                <p class="text-center">{{ recommendationMovie.title }}</p>
              </div>
            </div>
          </slide>
        </carousel>
    </div><hr>
    <div>
      <review-list-form v-if="!isReviewd"></review-list-form>
    </div>
    <div>
      <h4 class="fw-bold">[리뷰]</h4>
      <review-list :reviews="this.movie.review_set"></review-list>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { Carousel, Slide } from 'vue-carousel'
import Swal from 'sweetalert2'

import ReviewList from '@/components/ReviewList.vue'
import ReviewListForm from '@/components/ReviewListForm.vue'

export default {
  
  name: 'MovieDetail',
  data() {
    return {
      isUpdated: false
    }
  },
  props: { movieId: Number },
  components: {
    Carousel,
    Slide,
    ReviewList,
    ReviewListForm
  },
  computed: {
    ...mapGetters(['movie', 'recommendation', 'currentUser', 'profile']),
    isReviewd() {
      if(this.movie.seen_users && this.movie.seen_users.includes(this.currentUser.pk)) {
        return true
      }else{return false}
    },
    isWished() {
      if (this.movie.wish_users && this.movie.wish_users.includes(this.currentUser.pk)) {
        return true
      }else{return false}
    }
  },
  methods: {
    ...mapActions(['fetchMovie', 'wishMovie', 'seenMovie', 'updateProfile', 'fetchProfile']),
    onClickProfileUpdate(){
      const currentUser = this.currentUser
      Swal.fire(`내 인생영화가 ${this.movie.title}(으)로 변경되었습니다!`).then((res) => {
        if (res.isConfirmed){
          this.updateProfile({ tymi: this.profile.profile_set[0].tymi_image, room: this.profile.profile_set[0].room_image, user: this.currentUser.pk, life_movie: this.movie.title })
          window.location.href = `http://localhost:8080/home/${currentUser.username}`
        }
      }
      )
      
    },
    addWishList(movieId) {
      if(this.isWished) {
        this.wishMovie(movieId),
        Swal.fire(`위시리스트에서 제거되었습니다!`),
        this.fetchProfile(this.currentUser.username)
      }else{
        this.wishMovie(movieId),
        Swal.fire(`위시리스트에 추가되었습니다!`),
        this.fetchProfile(this.currentUser.username)
      }
    }
  },
  created() {
    this.fetchProfile(this.currentUser.username)
  }
}

</script>

<style>
.VueCarousel-wrapper {
  height: 300px;
}
#buttons:hover {
  cursor: pointer;
}
#genres {
  padding: 2px;
  border-radius: 10px;
  background-color: rgb(255, 232, 236);
  background-image: url('../assets/paper.jpg') no-repeat;
}
#title {
  font-size: 50px;
}
</style>