<template>
  <div>
    <p>Hello, {{ username }} </p>
    <div>
        <p>닉네임  {{ information.nickname }}</p>    
        <p>관심있는 장르  {{ information.interested + '아직 없음'}}</p>
        <p>등급  {{ information.grade }}</p>
        <p>프로필 이미지 <img :src="profileImage" alt="프로필 이미지"></p>  
    </div> 
    <button @click='goModify'>프로필 수정</button>
  </div>
</template>

<script>
import axios from 'axios'

const DJANGO_URL='http://127.0.0.1:8000'

export default {
    name : 'UserInformation',
    data(){
        return{
            information : '',
            profileImage : '',
        }
    },
    computed: {
        username() {
            return this.$store.state.username
        }
    },
    created(){
        axios({
            method:'get',
            url: `${DJANGO_URL}/api/v1/profile/${this.username}/`,
            headers: `Token ${this.$store.state.token}`
        })
            .then(res =>{
                // console.log(res)
                this.information = res.data
                this.profileImage = `${DJANGO_URL}` + res.data.profile_image
                // console.log(this.information)
            })
    },
    methods:{
        goModify(){
            this.$router.push({name: 'EditProfile', params: {username: this.username}})
        }
    }
}
</script>

<style>

</style>