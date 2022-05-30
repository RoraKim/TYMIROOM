<template>
  <div>
    <div>
      <review-list-item 
        v-for="review in reviews" 
        :review="review" 
        :key="review.id"
        class="m-3">
      </review-list-item>
    </div>

  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'

import { mapGetters } from 'vuex'

export default {
  name: 'ReviewList',
  components: { ReviewListItem },
  props: { reviews: Array },
  computed: {
    ...mapGetters(['movie', 'currentUser']),
  }
  
}
</script>

<style>

</style>