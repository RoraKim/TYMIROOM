<template>
  <div class="d-flex justify-content-center flex-row" id="background">
    <h1>로그아웃 되었습니다</h1>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    methods: {
      ...mapActions(['logout'])
    },
    computed: {
      ...mapGetters(['isLoggedIn'])
    },
    created() {
      if (this.isLoggedIn) {
        this.logout()
      } else {
        alert('잘못된 접근')
        this.$router.back()
      }
    },
  }
</script>

<style scoped>
#background { 
  background-color: #F9EEF5;
  text-align: center;
  height: 100vh;
  width: 100%;
  /* position: fixed; */
  overflow: hidden;
}

h1{
  margin: 300px;
  font-size: 5rem;
}
</style>