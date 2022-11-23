<template>
  <div>
    <UserInformation/>
  </div>
</template>

<script>

import UserInformation from '@/components/UserInformation'

export default {
  name: 'ProfileView',
  data() {
    return {
      profile: null,
    }
  },
  components:{
      UserInformation,
  },
  methods:{
  },
} 
</script>

<style>

</style>