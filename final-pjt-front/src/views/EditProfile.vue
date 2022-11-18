<template>
  <div>
    <h2>프로필 수정</h2>
    <form @submit.prevent='editProfile'>
      <div>
        <label for="nickname">닉네임</label>
        <input type="text" id='nickname' v-model='nickname'>
      </div>
      <br>
      <div>
        <label for="interested">관심장르</label>
        <input type="text" id='interested' v-model='interested'>
      </div>
      <div>
        <label for="upload">이미지 수정</label>
        <input multiple type="file" name='upload[]' ref='profileImg' accept="image/*">
      </div>
      <button @click='editProfile'>수정</button>
  </form>
  </div>
</template>

<script>
const DJANGO_URL='http://127.0.0.1:8000'
import axios from 'axios'
export default {
    name: 'EditProfile',
    data(){
      return{
        nickname : '',
        interested: '',
        profile_image: '',
      }
    },
    // computed:{
    //   isNickname(){
    //     return this.$store.state.nickname
    //   },
    //   isInterested(){
    //     return this.$store.state.interested
    //   },
    //   isImage(){
    //     return this.$store.state.profile_image
    //   }

    methods:{
      editProfile(){

        const nickname = this.nickname
        const interested = this.interested
        const profile_image = this.$refs.profileImg.files
        // console.log(this.$store.state.token)
        // this.edit.profile_image = this.$refs.profileImg.files
        const payload={
          nickname, interested, profile_image
        }
          // console.log('하하')
          axios({
            method: 'put',
            url: `${DJANGO_URL}/api/v1/profile/${this.$store.state.username}/`,
            headers:{
              Authorization : `Token ${this.$store.state.token}`,
              'Content-Type': 'multipart/form-data'
            },
            data: payload
          })
            .then( (res) =>{
              console.log(res)
              // this.$router.push({name: 'MyProfile'})
            })
            .catch(err =>{
              console.error(err)
            })
        }
      
    },
    
      
    
}
</script>

<style>

</style>