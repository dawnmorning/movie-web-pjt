<template>
  <div>
    <nav>
      <EditProfile/>
    </nav>
  </div>
</template>

<script>
const DJANGO_URL='http://127.0.0.1:8000'
import axios from 'axios'
import EditProfile from '@/components/EditProfile'

export default {
    name: 'EditProfileView',
    components:{
      EditProfile
    },

    methods:{
      editProfile(){
        const nickname = this.nickname
        const profile_image = this.$refs.profileImg.files
        // console.log(this.$store.state.token)
        // this.edit.profile_image = this.$refs.profileImg.files
        const payload={
          nickname,profile_image
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