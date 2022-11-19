<template>
  <div v-if='comments'>
    <div v-for="comment in comments" :key="comment.id">
        <CommentListItem
        :comment="comment"
        />
    </div>
  </div>
</template>

<script>
// const DJANGO_URL='http://127.0.0.1:8000'
// import axios from 'axios'
import CommentListItem from '@/components/CommentListItem'

export default {
    name: 'CommentList',
    props: {
        comments:Array,
    },
    components: {
        CommentListItem
    }
}
</script>

<style>

</style>