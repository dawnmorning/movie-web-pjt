<template>
<div>
    <div class='jua juaDetail' :style="`background-image: url(https://image.tmdb.org/t/p/w500/${review.movie.poster_path})`" v-if="review"></div>
        <!-- <div :style="`background-image: url(${review.movie.poster_path})`"></div> -->
        <div class="jua card reviewbody " style= 'font-size:20px;  width:1000px; left:18%; object-fit:cover;'>
            <p class="card-text">작성자 : {{review.author.nickname}}</p>
            <div class="card-body">
                <div><img class='img-fluid' :src='`https://image.tmdb.org/t/p/w500/${review.movie.poster_path}`'></div>
                <hr>       
                <h5 class="card-title">영화 : {{review.movie.title}}</h5>
                <hr>
                <div class="card-body" style='height:200px;'>
                    <div style='text-align:left; width:100%;'>
                        <h5 class="card-title" style=''>제목 : {{review.title}}</h5>
                        <h5 class="card-subtitle mb-2 text-muted">{{review.updated_at}}</h5>
                        <h5>별점 : {{review.rating}}</h5>
                        <!-- <star-rating class="card-subtitle mb-2 text-muted" :value='`${review.rating}`' :read-only='true'>별점 : {{review.rating}}</star-rating> -->
                        <p class="card-text">{{review.content}}</p>
                        <hr>
                        <h5>댓글 작성하기</h5>
                        <input type="text"
                        v-model="inputData"
                        @keyup.enter="createComment" 
                        >
                        <button
                        class='btn btn-btn-link' style=' color:black; text-decoration:none;'
                        @click="createComment"
                        >입력</button>
                        <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#exampleModal" style='display: flex; position:absolute; bottom:50px; left:120px; font-size:16px;'>
                            ...댓글보기
                        </button>
                    </div>
                </div>
                <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">댓글목록</h1>
                               
                            </div>
                            <div class="modal-body" style='padding:0'>
                                <div v-for="comment in comments" :key="comment.id">
                                        <CommentListItem
                                        :comment=comment
                                        style='text-align:left;'
                                        />
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>											</div>
                        </div>
                    </div>
                </div>
                <!-- 댓글 -->
                <!-- <div v-for="comment in comments" :key="comment.id">
                    <CommentListItem
                    :comment=comment
                    />
                </div> -->
                
            <button class='btn btn-btn-link' @click="goBack" style='color:black; text-decoration:none; float:right; font-size:20px; position:relative; bottom:50px;'>뒤로가기</button>
            </div>
        </div>
    </div>
</template>
<script>
// import axios from 'axios'
// const DJANGO_URL='http://127.0.0.1:8000'
import CommentListItem from '@/components/CommentListItem'
// import StarRating from 'vue-star-rating'
export default {
    name: 'ReviewDetail',
    data() {
        return {
            inputData: null,
        }
    },
    computed: {
        review() {
            const review_id = Number(this.$route.params.review_id)
            const myReview = this.$store.state.reviews.find( function(review) {
                if (review.id === review_id) {
                    return true
                }
            })            
            return myReview
        },
        comments() {
            return this.review.comments
        }
    },
    components: {
        CommentListItem,
        // StarRating
    },
    methods: {
        goBack() {
            this.$router.go(-1)
        },
        createComment() {
            const payload = {
                review_id: this.$route.params.review_id,
                comment: this.inputData,
            }
            this.$store.dispatch('createComment', payload)
            this.inputData = null
        },

    },
}
</script>

<style>
.juaDetail{
    position: absolute;
    top: 0;
    left: 0;
    filter: blur(3px) brightness(160%) contrast(30%);
    width: 100%;
    height: 180%;
    background-size: cover;
    margin-top:-155px;
    transform: translateY(-120px);
    
}
</style>