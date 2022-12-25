<template>
  <nav class='navWrap'>
    <div class='contentsWrap ' style='font-size:20px; margin-top:0;'>
 
        <form @submit.prevent="uploadProfile" class='formWrap animate__animated animate__fadeIn'>
            <!-- <div class="jua"></div> -->
            <div class='editWindow jua' style='background-color:white;'>
              <h1 style='margin-top:10px; margin-bottom:-5px;'>프로필 수정</h1>

              <div class="profile" v-if='nickname' >
                <div class="profile_img" style='background-color:white;'>
                    <img style='width:185px;' :src="profileImage" alt="프로필 이미지">
                </div>
              </div>
              <div v-if='filename'>

              <div  v-for='(file, idx) in filename' :key='idx'>
                   {{file[1]}}
              </div>
              </div>
              <div class="">
                <div style='font-size: 15px; text-align:left; position:relative; left:80px;'>
                    <div style="margin-bottom: 10px;">
                      <label style='margin-right:100px;' for="" class=''>아이디</label>
                      <span style=''>{{username}}</span>
                    </div>
                    <div style="margin-bottom: 10px;">
                      <label  for="" class='' style='margin-right:100px;'>이메일</label>
                      <span style=' '>{{ email }}</span>
                    </div>
                    <div style="margin-bottom: 10px;">
                      <label style='margin-right:100px;' for="">닉네임</label>
                      <span style='  '>{{ nickname }}</span>
                    </div>
                    <div class='filebox' style="margin-bottom: 40px;">
                      <input class="upload-name" :value="filename" placeholder="첨부파일" >
                      <label for="file" style='margin-top:10px; position:relative; left:-8px;'>파일찾기</label> 
                      <input type="file"
                      id="file"
                        accept="image/jpeg/*"
                        @change="uploadImage"
                        />
                    </div>
                </div>
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
        filename:null,
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
      },

    },
    methods:{
      showname(){
        console.log(this.$store.state.username)
      },
      backprofile(){
        this.$router.push({name: 'ProfileView'})
      },
      uploadImage(e) {
        
        this.filename = e.target.files[0].name
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
    height: 80%;
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
.filebox .upload-name {
    display: inline-block;
    height: 40px;
    padding: 0 10px;
    vertical-align: middle;
    border: 1px solid #dddddd;
    width: 78%;
    color: #999999;
}
.filebox label {
    display: inline-block;
    padding: 10px 20px;
    color: #fff;
    vertical-align: middle;
    background-color: #999999;
    cursor: pointer;
    height: 40px;
    margin-left: 10px;
}
.filebox input[type="file"] {
    position: absolute;
    width: 0;
    height: 0;
    padding: 0;
    overflow: hidden;
    border: 0;
}
</style>