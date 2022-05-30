<template>
<div>
  <!-- 내 글 -->
  <div id="border" class="p-3" style=" background-color:#fddce0;" v-if="currentUser.username === review.user.username">
    <div class="d-flex justify-content-between">
      <div style="width: 250px" class="d-flex justify-content-between">
        <a :href="'http://localhost:8080/home/'+review.user.username" class="text-decoration-none fs-5 px-2">
          <img src="../assets/home.png" class="inline" style="width: 30px;">
          <span class="fs-4 px-2">{{ review.user.username }}</span>
        </a>
        <div style="width: 100px">
          <img src="../assets/star/full.png" style="width:20px;" v-for="a in review.score" :key="a">
        </div>
      </div>
      <div>
        <span v-if="currentUser.username === review.user.username">
          <span class="fs-4 ps-1">내 리뷰의 좋아요 수 : </span>
          <img src="../assets/heart/full.png" style="width:30px; height:auto;">
          <span class="fs-4 ps-1">X {{ review.like_users.length }}</span>
        </span>
        <span v-else>
          <img src="../assets/heart/full.png" @click="likeReview(payload)" v-if="isLiked" style="width:30px; height:auto;">
          <img src="../assets/heart/empty.png" @click="likeReview(payload)" v-else  style="width:30px; height:auto;">
          <span class="fs-4 ps-1">X {{ review.like_users.length }}</span>
        </span>
      </div>
    </div><hr>
      
    <div v-if="currentUser.username === review.user.username">
      <div v-if="!isEditing">
        <div class="m-2">
          <span class="fs-4">{{ payload.content }}</span>
        </div>
        <div>
          <span>
            <button @click="switchIsEditing">수정</button> |
            <button @click="onDelete">삭제</button>
          </span>
        </div>
      </div>
      <div v-else>
        <div class="m-2">
          <input type="text" class="form-control p-2 fs-4" v-model="payload.content">
            <div class="star-rating">
            <input type="radio" id="5-stars" name="rating" value="5" v-model="payload.score">
            <label for="5-stars" class="star"></label>
            <input type="radio" id="4-stars" name="rating" value="4" v-model="payload.score">
            <label for="4-stars" class="star"></label>
            <input type="radio" id="3-stars" name="rating" value="3" v-model="payload.score">
            <label for="3-stars" class="star"></label>
            <input type="radio" id="2-stars" name="rating" value="2" v-model="payload.score">
            <label for="2-stars" class="star"></label>
            <input type="radio" id="1-star" name="rating" value="1" v-model="payload.score">
            <label for="1-star" class="star"></label>
          </div>
        </div>
        <div>
          <button @click="onUpdate">제출</button> |
          <button @click="switchIsEditing">취소</button>
        </div>
      </div>
    </div>
    <div v-else>
      <div class="m-2">
        <span class="fs-4">{{ payload.content }}</span>
      </div>
    </div>
  </div>
 <!-- 딴 사람 -->
    <div id="border" class="p-3" style=" background-color:#F4F3F3;" v-else>
    <div class="d-flex justify-content-between">
      <div style="width: 250px" class="d-flex justify-content-between">
        <a :href="'http://localhost:8080/home/'+review.user.username" class="text-decoration-none fs-5 px-2">
          <img src="../assets/home.png" class="inline" style="width: 30px;">
          <span class="fs-4 ps-2">{{ review.user.username }}</span>
        </a>
        <div style="width: 100px">
          <img src="../assets/star/full.png" style="width:20px;" v-for="a in review.score" :key="a">
        </div>
      </div>
      <div>
        <span v-if="currentUser.username === review.user.username">
          <img src="../assets/heart/full.png" style="width:30px; height:auto;">
          <span class="fs-4 ps-1">X {{ review.like_users.length }}</span>
        </span>
        <span v-else>
          <img src="../assets/heart/full.png" @click="likeReview(payload)" v-if="isLiked" style="width:30px; height:auto;">
          <img src="../assets/heart/empty.png" @click="likeReview(payload)" v-else  style="width:30px; height:auto;">
          <span class="fs-4 ps-1">X {{ review.like_users.length }}</span>
        </span>
      </div>
    </div><hr>
      
    <div v-if="currentUser.username === review.user.username">
      <div v-if="!isEditing">
        <div class="m-2">
          <span class="fs-4">{{ payload.content }}</span>
        </div>
        <div>
          <span>
            <button @click="switchIsEditing">수정</button> |
            <button @click="onDelete">삭제</button>
          </span>
        </div>
      </div>
      <div v-else>
        <div class="m-2">
          <input type="text" class="form-control p-2 fs-4" v-model="payload.content">
            <div class="star-rating">
            <input type="radio" id="5-stars" name="rating" value="5" v-model="payload.score">
            <label for="5-stars" class="star"></label>
            <input type="radio" id="4-stars" name="rating" value="4" v-model="payload.score">
            <label for="4-stars" class="star"></label>
            <input type="radio" id="3-stars" name="rating" value="3" v-model="payload.score">
            <label for="3-stars" class="star"></label>
            <input type="radio" id="2-stars" name="rating" value="2" v-model="payload.score">
            <label for="2-stars" class="star"></label>
            <input type="radio" id="1-star" name="rating" value="1" v-model="payload.score">
            <label for="1-star" class="star"></label>
          </div>
        </div>
        <div>
          <button @click="onUpdate">제출</button> |
          <button @click="switchIsEditing">취소</button>
        </div>
      </div>
    </div>

    <div v-else>
      <div class="m-2">
        <span class="fs-4">{{ payload.content }}</span>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import Swal from 'sweetalert2'


export default {
  name: 'ReviewListItem',
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        movieId: this.review.movie,
        reviewId: this.review.id,
        content: this.review.content,
        score: this.review.score
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'movie', 'profile']),
    isLiked() {
      if(this.review.like_users && this.review.like_users.includes(this.currentUser.pk)) {
        return true
      }else {return false}
    }
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview', 'likeReview', 'seenMovie', 'fetchMovie', 'updateProfile', 'fetchProfile']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    },
    onDelete() {
      const payload = this.payload
      const currentUser = this.currentUser
      const exp = this.profile.profile_set[0].exp
      Swal.fire(`내 리뷰가 삭제되었습니다!`).then((res) => {
        if (res.isConfirmed){
          this.deleteReview(payload)
          this.updateProfile({ user: currentUser.pk, exp: exp - 1 })
          this.seenMovie(payload.movieId)
          this.fetchProfile(currentUser.username)
          window.location.href = `http://localhost:8080/movies/recommend`
        }
      })
    }
  },
  // created() {
  //   this.fetchProfile(this.currentUser.username)
  // }

}
</script>

<style>
.star-rating {
  
  display:flex;
  flex-direction: row-reverse;
  font-size:1.5em;
  justify-content:space-around;
  padding:0 .2em;
  text-align:center;
  width:5em;
}

.star-rating input {
  display:none;
}

.star-rating label {
  width: 1em;
  height: 1em;
  background-image: url('../assets/star/empty.png');
  background-size: cover;
}

.star-rating :checked ~ label {
  background-image: url('../assets/star/full.png');
  background-size: cover;
}

.star-rating label:hover,
.star-rating label:hover ~ label {
  background-image: url('../assets/star/full.png');
  background-size: cover;
}
</style>