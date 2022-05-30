<template>
  <form @submit.prevent="onSubmit" class="guestbook-list-form">
    <div class="d-flex">
      <label for="guestbook" class="fs-4"></label>
      <input type="text" id="guestbook" placeholder="방명록을 입력하세요" class="form-control mx-2 fs-4" v-model="content" required>
      <button class="btn-light f-rounded-end fs-4 pt-1 mt-1" style="width:70px;">제출</button>
    </div>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'GuestbookListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['profile']),
  },
  methods: {
    ...mapActions(['createGuestbook']),
    onSubmit() {
      this.createGuestbook({ username: this.profile.username, content: this.content})
      this.content = ''
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
</style>