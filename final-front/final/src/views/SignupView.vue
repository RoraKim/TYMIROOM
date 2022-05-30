<template>
  <div id="background">
    <img src="../assets/small_logo1.png" alt="image logo">
      <div class="text-center">
        <account-error-list v-if="authError"></account-error-list>
      </div>
      <div class="d-flex justify-content-center" style="margin:50px">

      <form @submit.prevent="signup(credentials)">
        <div>
          <h1 class="fw-bold">SIGN UP</h1>
          <label for="username">아이디</label><br>
          <input  v-model="credentials.username" type="text" id="username" required style="" placeholder="아이디를 입력하세요" class="p-4 fs-4 mt-1"/>
        </div>
        <div>
          <label for="password1">비밀번호</label><br>
          <input v-model="credentials.password1" type="password" id="password1" required style="" placeholder="비밀번호를 입력하세요" class="p-4 fs-4 mt-1"/>
        </div>
        <div>
          <label for="password2" style="">비밀번호 확인</label><br>
          <input v-model="credentials.password2" type="password" id="password2" required style="" placeholder="비밀번호를 다시 입력하세요" class="p-4 fs-4 mt-1"/>
        </div>
        <div>
          <button>Signup</button>
          <router-link to="/" class="link"><button>돌아가기</button></router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountsErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
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
form { 
/* Rectangle 2 */


/* position: absolute; */
width: 450px;
height: 530px;
left: 910px;
text-align: center;
top: 450px;

background: #EA8D98;
box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
border-radius: 10px;
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
input {
  /* position: absolute; */
width: 280px;
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

img { 
  width: 1000px;
  margin-top: 50px;
}
</style>