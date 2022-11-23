<template>
  <nav class='navWrap'>
    <div class='contentsWrap ' style='font-size:20px; margin-top:0;'>
        <form @submit.prevent='signUp' class = 'formWrap animate__animated animate__fadeIn'>
            <!-- <div class="jua"></div> -->
            <div class='editWindow jua' style=''>
                <h1 style='margin-top:30px;'>프로필 수정</h1>
                <div class="inlineToBlock">
                  <div>
          
                      <label for="" class='labeleft'>아이디</label>
                      <span style='font-size: 20px; margin-left:20px;'>{{username}}</span>
                    
                      <br>
                      <label for="" class='labeleft' style= 'margin-left:-3px;'>이메일</label>
                      <span style='font-size: 15px;  margin-left:20px;'>{{ email }}</span>
                    
                  </div>
                    <div style='margin-top:20px;'>
                      <label for="">닉네임</label>
                      <input type="text" id='nickname' v-model.trim='nickname' class='id' style='margin-left:50px;'>
                    </div>
                </div>
                <div class='inlineToBlock'>
                     <button class="button btnPush btnBlueGreen">사진 수정하기</button>
                     <input class="inputfile" @change="upload" accept="image/jpg" type="file" id="file"/>
                </div>
                <br>
                <br>
                <div class="inlineToBlock">
                  <button class='Btn btnPush btnBlueGreen' type="submit" style='margin-top:0 margin-left:30px;'>프로필 수정</button>
                  <button @click='backprofile' class='Btn btnPush btnBlueGreen' type="submit" style='margin-top:0'>취소</button>
                </div>
                <!-- <button>뒤로 가기</button> -->
                <!-- {{ email }} -->
            </div>
        </form>
    </div>
      
  </nav>
</template>

<script>
export default {
    name:'EditProfile',
    data(){
      return{
        // nickname: '',
        profile_image: '',
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
          return this.$store.state.profile_image
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
      upload(e){
        var file = e.target.files;
        console.log(file)
        
        // let url = URL.createObjectURL(file[0]);
        // this.image = url;

      },
      updateProfile(){
        this.$store.dispatch('updateProfile', file)
        
      }
    }
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
</style>