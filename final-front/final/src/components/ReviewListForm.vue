<template>

  <div>
    <form @submit.prevent="onSubmit" class="review-list-form">
      <div class="d-flex">
        <div class="star-rating">
          <input type="radio" :id="'5-stars'+movie.movie_id" name="rating" :value="5" @click="updateStar" :checked='this.star==5'>
          <label :for="'5-stars'+movie.movie_id" class="star"></label>
          <input type="radio" :id="'4-stars'+movie.movie_id" name="rating" :value="4" @click="updateStar" :checked='this.star==4'>
          <label :for="'4-stars'+movie.movie_id" class="star"></label>
          <input type="radio" :id="'3-stars'+movie.movie_id" name="rating" :value="3" @click="updateStar" :checked='this.star==3'>
          <label :for="'3-stars'+movie.movie_id" class="star"></label>
          <input type="radio" :id="'2-stars'+movie.movie_id" name="rating" :value="2" @click="updateStar" :checked='this.star==2'>
          <label :for="'2-stars'+movie.movie_id" class="star"></label>
          <input type="radio" :id="'1-stars'+movie.movie_id" name="rating" :value="1" @click="updateStar" :checked='this.star==1'>
          <label :for="'1-stars'+movie.movie_id" class="star"></label>
        </div>
        <input type="text" id="review" placeholder="리뷰를 입력하세요" class="form-control mx-2" v-model="content" required>
        <button class="">review</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import Swal from 'sweetalert2'

export default {
  name: 'ReviewListForm',
  data() {
    return {
      content: '',
      score: 3,
    }
  },
  computed: {
    ...mapGetters(['movie', 'currentUser', 'star', 'profile']),
  },
  methods: {
    ...mapActions(['createReview', 'seenMovie', 'fetchProfile', 'fetchStar', 'fetchMovie', 'updateProfile']),
    onSubmit() {
      this.createReview({ movieId: this.movie.movie_id, content: this.content, score: this.star})
      this.seenMovie(this.movie.movie_id)
      if(this.profile.profile_set[0].level === 0 && this.profile.profile_set[0].exp === 9) {
        Swal.fire({
          icon: 'success',
          title: '레벨업! 축하합니다!',
          text: '관리 페이지에서 더 많은 티미를 만나보세요!'
        })
        this.updateProfile({ user: this.currentUser.pk, exp:this.profile.profile_set[0].exp + 1, level: 1 })
      }else{
        this.updateProfile({ user: this.currentUser.pk, exp: this.profile.profile_set[0].exp + 1 })
      }
      this.fetchProfile(this.currentUser.username)
      this.content = ''
      this.fetchStar(3)
    },
    updateStar(event) {
      console.log(event.target)
      this.fetchStar(event.target.value)
    }
  }
}
</script>

<style>
.comment-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}

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

.star-rating :active ~ label {
  background-image: url('../assets/star/full.png');
  background-size: cover;
}

.star-rating label:hover,
.star-rating label:hover ~ label {
  background-image: url('../assets/star/full.png');
  background-size: cover;
}
</style>