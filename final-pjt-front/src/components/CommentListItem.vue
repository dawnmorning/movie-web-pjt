<template>
  <div>
    <hr>
    {{ comment.author }} |
    {{ comment.content }}
    <button
    @click="deleteComment(comment)"
    >X</button>

    
  </div>
</template>

<script>
export default {
    name:'CommentListItem',
    props: {
        comment: Object,
    },
    methods: {
        deleteComment(comment) {
            console.log(this.$store.state.reviews)
            
            this.$store.dispatch('deleteComment', comment)  
            console.log(this.$store.state.reviews)
        }
    }
}
</script>

<style>

</style>