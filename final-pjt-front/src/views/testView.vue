<template>
  <div style='margin-top:400px;'>
    <star-rating id=setstar :star-size="30" v-model="rating" :border-width="5" border-color="#d8d8d8" 
    :rounded-corners="true" 
    :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]">
    </star-rating>
    <div class="modal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>Modal body text goes here.</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Save changes</button>
          </div>
        </div>
      </div>
</div>
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