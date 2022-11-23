<template>
  <nav class='navWrap'>
    <div class='contentsWrap ' style='font-size:20px; margin-top:0;'>
        <form @submit.prevent="uploadProfile" class='formWrap animate__animated animate__fadeIn'>
            <!-- <div class="jua"></div> -->
            <div class='editWindow jua' style=''>
              <h1 style='margin-top:30px;'>프로필 수정</h1>

              <div class="profile" v-if='nickname'>
                <div class="profile_img">
                    <img :src="profileImage" alt="프로필 이미지">
                </div>
              </div>

              <div class="inlineToBlock">
                <div>
                    <div style="text-align: start;">
                      <label for="" class='labeleft'>아이디</label>
                      <span style='font-size: 20px; margin-left:20px;'>{{username}}</span>
                    </div>
                    <div>
                      <label for="" class='labeleft' style= 'margin-left:-3px;'>이메일</label>
                      <span style='font-size: 15px;  margin-left:20px;'>{{ email }}</span>
                    </div>
                </div>

                <div style='margin-top:20px;'>
                  <label for="">닉네임</label>
                  <span style='font-size: 15px;  margin-left:20px;'>{{ nickname }}</span>
                    <!-- <input type="text" id='nickname' v-model.trim='nickname' class='id' style='margin-left:50px;'> -->
                </div>
              </div>

              <div class='inlineToBlock'>
                <!-- <button class="button btnPush btnBlueGreen">사진 수정하기</button>
                -->
                <input type="file"
                  accept="image/jpeg/*"
                  @change="uploadImage"
                  
                />
                <!-- <input class="inputfile" @change="upload" accept="image/jpg" type="file" id="file"/> -->
              </div>

              <div class="inlineToBlock">
                <button class='Btn btnPush btnBlueGreen' type="submit" style='margin-top:0 margin-left:30px;'>프로필 수정</button>
                <button @click='goBack' class='Btn btnPush btnBlueGreen' type="submit" style='margin-top:0'>취소</button>
              </div>

            </div>
        </form>
    </div>
      
  </nav>
</template>

<script>
const DJANGO_URL='http://127.0.0.1:8000'


export default {
    name:'EditProfile',
    data(){
      return{
        // nickname: '',
        profile_image: '',
        file: null,
      }
    },
    computed:{
      username() {
        return this.$store.state.username
      },
      nickname(){
          return this.$store.state.nickname
      },
      profileImage(){
          return DJANGO_URL + this.$store.state.profile_image
      },
      email(){
        return this.$store.state.email
      }
    },
    methods:{
      showname(){
        console.log(this.$store.state.username)
      },
      backprofile(){
        this.$router.push({name: 'ProfileView'})
      },
      uploadImage(e) {
        
        let fd = new FormData();
        fd.append('profile_image', e.target.files[0])
        this.file = fd
        
      },
      uploadProfile(){
        this.$store.dispatch('uploadProfile', this.file)
        this.file = null
      },
      
      goBack() {
        this.$router.go(-1)
      }
    },
}
</script>

<style>
div .Btn{
  display: block;
  position: relative;
  float: left;
  width: 120px;
  padding: 0;
  margin-left: 70px;
  font-weight: 600;
  text-align: center;
  line-height: 50px;
  color: #FFF;
  border-radius: 5px;
  transition: all 0.2s ;
  justify-content: center;
}
div .editWindow {
    margin-top: 30%;
    /* padding:1px; */
    overflow: hidden;
    background-color: #fcfcfc;
    padding: 10px auto;
    height: 500px;
    width: 450px;
    justify-content: center;
    border: 1px solid #dfdfdf;
    border-radius: 3px;
}
div .button {
  display: block;
  position: relative;
  float: left;
  width: 120px;
  padding: 0;
  margin: 30px 20px 10px 35%;
  font-weight: 600;
  text-align: center;
  line-height: 50px;
  color: #FFF;
  border-radius: 5px;
  transition: all 0.2s ;
  justify-content: center;
}
.btnBlueGreen {
  background: #00AE68;
}
.btnBlueGreen.btnPush {
  box-shadow: 0px 5px 0px 0px #007144;
}
.btnBlueGreen.btnPush:hover {
  box-shadow: 0px 0px 0px 0px #007144;
}
div .alreadyBlock{
  left:50%;
}
.labeleft{
  margin-left: -110px;
  margin-right: 60px;
}

.profile {
    display: flex;
    align-items: center;
    margin-bottom: 35px;
}
.profile .profile_img {
    margin: 0 70px;
}
.profile .profile_img img {
    width: 150px;
    height: 150px;
    border-radius: 50%;
}
</style>