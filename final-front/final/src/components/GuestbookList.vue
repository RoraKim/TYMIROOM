<template>
  <div class="p-3">
    
    <guestbook-list-form v-if="this.currentUser.username !== this.$route.params.username"></guestbook-list-form>
    
    <table class="table table-borderless table-hover">
      <tbody v-if="guestbooks[0]">
        <guestbook-list-item 
          v-for="guestbook in guestbooks.slice().reverse()" 
          :guestbook="guestbook" 
          :key="guestbook.id">
        </guestbook-list-item>
      </tbody>
      <h4 v-else class="pt-3 mb-0 text-center">아직 방명록이 없어요,, 방명록을 남겨주세요!</h4>
    </table>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'


import GuestbookListForm from '@/components/GuestbookListForm.vue'
import GuestbookListItem from '@/components/GuestbookListItem.vue'

export default {
  name: 'GuestbookList',
  components: { GuestbookListForm, GuestbookListItem },
  computed: {
    ...mapGetters(['currentUser','profile']),
  },
  props: { guestbooks: Array },
}
</script>

<style>

</style>