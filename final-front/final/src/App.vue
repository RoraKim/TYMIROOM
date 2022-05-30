<template>
  <div id="app back">
    <nav class="navbar navbar-expand-md bg-white d-flex justify-content-between">
    <div class="container-fluid">
      <img src="./assets/small_logo1.png" alt="image logo">
      <div>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="d-flex align-items-center mb-0 navbar-nav me-auto mb-2 mb-lg-0" v-if="isLoggedIn">
            <li class="nav-item px-1">
              <a :href="'http://localhost:8080/home/'+currentUser.username" style="text-decoration: none;">Home</a></li>
            <li class="nav-item px-1"><router-link to="/logout" style="text-decoration: none;">logout</router-link></li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
         <!-- <nav>
      <img alt="small_logo" src="./assets/small_logo.png">
      <h1>login</h1>

    </nav> -->
    
    <router-view/>
  
    <!-- <div class="app_body">
      
    </div> -->


  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default ({
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser'])
  }  
})
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  position: absolute;
}

nav a {

  font-weight: bold;
  font-size: 25px;
  color: #2c3e50;
}

img {
  width: 200px;
  padding-bottom: 10px;
}

button:active {
   box-shadow: 1px 1px 0 rgb(0,0,0,0.5); 
   position: relative; top:2px;
   background-color: antiquewhite;

}
.back {
  background-color: darkgray;
  /* background-size: 80%; */
  height: 100%;
  width: 100%;
  /* position: fixed; */
  overflow: hidden;
}
.app_body {
  background-color: darkgrey;
  background-size: 100%;
  height: 130vh;
}
</style>
