<template>
  <div>
    {{ myReview }}
    <a href="">
      <div class="board_img">
          <img src="" alt="이미지">
      </div>
    </a>
  </div>
</template>

<script>
export default {
  name: 'MyReviewItem',
  props: {
    myReview: Object,
  },
  data() {
    return {
      poster_image() { return  }
    }

  }
}

</script>

<style>

</style>