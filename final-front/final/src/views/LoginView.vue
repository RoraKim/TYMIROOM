<template>
  <div id="background">


    <img src="../assets/small_logo1.png" alt="image logo">


    <account-error-list v-if="authError"></account-error-list>

    <div class="d-flex justify-content-center" style="margin:100px">
    <form @submit.prevent="login(credentials)">
      <div>
        <h1 class="fw-bold">LOGIN</h1>
        <label for="username" >아이디</label><br>
        <input v-model="credentials.username" type="text" id="username" required style="" placeholder="아이디를 입력하세요" class="p-4 fs-4 mt-1"/>
      </div>

      <div>
        <label for="password">비밀번호</label><br>
        <input v-model="credentials.password" type="password" id="password" required style="" placeholder="비밀번호를 입력하세요" class="p-4 fs-4 mt-1 "/>
      </div>

      <button>로그인</button>
      <router-link to="/signup" class="link"><button>회원 가입</button></router-link>
    </form>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountsErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style scoped>
#background { 
  background-color: #F9EEF5;
  text-align: center;
  height: 94vh;
  width: 100%;
  /* position: fixed; */
  overflow: hidden;
}

img { 
  width: 1000px;
  margin-top: 50px;
}

form { 
/* Rectangle 2 */


/* position: absolute; */
width: 420px;
height: 420px;
left: 910px;
text-align: center;
top: 450px;

/* EA8D98/darkpink */

background: #EA8D98;
box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
border-radius: 10px;
}

input {
  /* position: absolute; */
width: 260px;
height: 40px;
left: 537px;
top: 258px;
margin-top:25px;
margin-bottom: 20px;

/* #FCFEFF/white */

background: #FCFEFF;
box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
border-radius: 10px;
border: #FCFEFF;
}

h1{ 
  margin: 20px;
}

label{
  font-size: 1.5rem;
  display:inline;
}

button { 
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);
  height: 40px; width: 135px;
  border: #EA8D98;
  background: #FCFEFF;
  border-radius: 10px;
  margin: 30px;
  font-size: 20px;
  
}

</style>