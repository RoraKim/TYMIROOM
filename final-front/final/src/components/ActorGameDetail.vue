
<template>
<div v-if="!!actor" style="width:300px">
  <!-- <div> -->
  <div class="card shadow">
    <img :src="'https://image.tmdb.org/t/p/original/' + actor.profile_path" class="card-img-top p-2 mb-1" alt="..." style="height: 500px; width:300px;" @click="select">
    <div class="card-body">
      <h3 class="card-title text-center">{{ actor.name }}</h3>
    </div>
  </div>
  <h3 class="text-center pt-2">{{ actor.name }}</h3>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ActorGameDetail',
  data() {
    return {
      movieObject: null,
      disabled: false,
      openDelay: '0',
      closeDelay: '0',
      value: false,
    }
  },

   props: {
    actor:{
      type: Object,
      required: false,
    }
  },

  components: {  },

  computed: {
    ...mapGetters(['currentUser', 'movies', 'recommendation', 'profile'])
    },
  methods: {
    ...mapActions(['fetchActor','fetchActorGames','updateProfile', 'fetchProfile']),
    // searchMovies() {
    //   this.fetchMovieGames()
    // },

    select() {
      this.$emit('choiceEvent', true)
    }
  },

  created() {
    // this.fetchCurrentUser()
    this.fetchActorGames(),
    console.log(this.actor.name)
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