<template>
  <div>
    <div class="d-flex justify-content-between">
      <h1>{{ actor.name }}</h1>
    </div>
    <hr>
    <div class="d-flex">
      <div>
        <img :src="'https://image.tmdb.org/t/p/original/' + actor.profile_path" >
      </div>
      <div class="mx-5" style="width: 70%;">
        <h4 class="fw-bold">[출연작]</h4>
        <carousel 
        :perPage="4"
        :navigationEnabled="true"
        :paginationPadding="5"
        :speed="300"
        class="active my-4">
          <slide v-for="movie in actor.actor_movies" :key="movie.id" class="active">
            <div class="card d-flex row justify-content-center mx-2">
              <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" style="height: 250px;">
            </div>
          </slide>
        </carousel>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { Carousel, Slide } from 'vue-carousel'

// import ReviewList from '@/components/ReviewList.vue'
// import ReviewListForm from '@/components/ReviewListForm.vue'

export default {
  
  name: 'ActorDetail',
  data() {
    return {
      isUpdated: false
    }
  },
  props: { actorId: Number },
  components: {
    Carousel,
    Slide,
  },
  computed: {
    ...mapGetters(['actor', 'recommendation', 'currentUser', 'profile']),

  },
  methods: {
    ...mapActions(['fetchProfile']),
  },
}

</script>

<style>
.VueCarousel-wrapper {
  height: 300px;
}

.img {
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}
</style>