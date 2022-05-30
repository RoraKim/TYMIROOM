<template>
  <div class="account-error-list">
    <p v-for="(errors, field) in authError" :key="field">
      <ul style="list-style-type: none; padding:0;">
        <li v-for="(error, idx) in errors" :key="idx">
          <span class="fs-4">{{ error }}</span>
        </li>
      </ul>
    </p>

  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    },
  }
</script>

<style>
  .account-error-list {
    color: red;
  }
</style>
