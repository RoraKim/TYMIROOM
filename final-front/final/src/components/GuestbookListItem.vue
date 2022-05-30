<template>
<div>
  <div class="border border-2 rounded-4 d-flex row m-2" style="background-color:#e4f0fa;" v-if="currentUser.username === guestbook.friend.username">
    <div class="d-flex justify-content-between border-bottom pb-0">
      <div>
        <p class="fs-3 ps-2">
          {{ guestbook.friend.username }} - 
          <span class="fs-5">{{ guestbook.created_string }}</span>
        </p>
      </div>
        
      <div v-if="currentUser.username === guestbook.friend.username">
        <div v-if="!isEditing">
          <span>
            <button @click="switchIsEditing" class="btn-light f-rounded-end mt-1" style="width:55px; height:35px;">수정</button> |
            <button @click="deleteGuestbook(payload)" class="btn-light f-rounded-end" style="width:55px; height:35px;">삭제</button>
          </span>
        </div>
        <div v-else>
          <span>
            <button @click="onUpdate" class="btn-light f-rounded-end mt-1" style="width:55px; height:35px;">제출</button> |
            <button @click="switchIsEditing" class="btn-light f-rounded-end" style="width:55px; height:35px;">취소</button>
          </span>
        </div>
      </div>
      <div v-else>
        <a :href="'http://localhost:8080/home/'+guestbook.friend.username" class="text-decoration-none">
          <img src="../assets/home.png" class="inline" style="width: 30px;">
          <span style="color:black;"> 친구의 티미룸으로 이동</span>
        </a>
      </div>
    </div>
    
    <div v-if="!isEditing">
      <span class="p-2 fs-4">{{ payload.content }}</span>
    </div>
    <div v-else>
      <input type="text" class="form-control p-2 fs-4" v-model="payload.content">
    </div>
  </div>

  <div class="border border-2 rounded-4 d-flex row m-2" style="background-color:white;" v-else>
    <div class="d-flex justify-content-between border-bottom pb-0">
      <div>
        <p class="fs-3 ps-2">
          {{ guestbook.friend.username }} - 
          <span class="fs-5">{{ guestbook.created_string }}</span>
        </p>
      </div>
        
      <div v-if="currentUser.username === guestbook.friend.username">
        <div v-if="!isEditing">
          <span>
            <button @click="switchIsEditing" class="btn-light f-rounded-end mt-1" style="width:55px; height:35px;">수정</button> |
            <button @click="deleteGuestbook(payload)" class="btn-light f-rounded-end" style="width:55px; height:35px;">삭제</button>
          </span>
        </div>
        <div v-else>
          <span>
            <button @click="onUpdate" class="btn-light f-rounded-end mt-1" style="width:55px; height:35px;">제출</button> |
            <button @click="switchIsEditing" class="btn-light f-rounded-end" style="width:55px; height:35px;">취소</button>
          </span>
        </div>
      </div>
      <div v-else>
        <a :href="'http://localhost:8080/home/'+guestbook.friend.username" class="text-decoration-none">
          <img src="../assets/home.png" class="inline" style="width: 30px;">
          <span style="color:black;"> 친구의 티미룸으로 이동</span>
        </a>
      </div>
    </div>
    
    <div v-if="!isEditing">
      <span class="p-2 fs-4">{{ payload.content }}</span>
    </div>
    <div v-else>
      <input type="text" class="form-control p-2 fs-4" v-model="payload.content">
    </div>
  </div>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'GuestbookListItem',
  props: { guestbook: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        username: this.$route.params.username,
        guestbookId: this.guestbook.id,
        content: this.guestbook.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateGuestbook', 'deleteGuestbook']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateGuestbook(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
</style>