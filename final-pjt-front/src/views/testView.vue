<template>
  <div style='margin-top:400px;'>
    <star-rating id=setstar :star-size="30" v-model="rating" :border-width="5" border-color="#d8d8d8" 
    :rounded-corners="true" 
    :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]">
    </star-rating>

  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
export default {
  name:'textView',
  components:{
    StarRating
  }
}
</script>

<style>

</style>