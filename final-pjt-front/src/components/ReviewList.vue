<template>
  <div class="container" v-if="reviews">
    <div v-for="review in reviews" :key="review.id">
        <ReviewListItem
        :review=review
        />
    </div>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem'
export default {
    name:'ReviewList',
    components: {
        ReviewListItem,
    },
    computed:{
      reviews(){
        return this.$store.state.reviews
      }
    },
    created() {
      this.$store.dispatch('getReviews')
    }
}
</script>

<style>

</style>