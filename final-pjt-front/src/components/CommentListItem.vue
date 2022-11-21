<template>
  <div>
    <hr>
    {{ comment.author.nickname }} |
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
            this.$store.dispatch('deleteComment', comment)  
        }
    }
}
</script>

<style>

</style>