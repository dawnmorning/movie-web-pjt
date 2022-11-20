<template>
  <nav>
    <div class='contentsWrap animate__animated animate__slideInDown delay-5s slower' style='margin-top : 20px; height : 100px;' >
        <form @submit.prevent='logIn' class=''>
          <div class='loginWindow jua' style= 'margin-top:70px;'>
            <br>
            <h1>로그인</h1>
            <input type="text"
            class='inlineToBlock'
            placeholder='아이디'
            v-model='username'
            >
            
            <input type="password" 
            class='inlineToBlock' 
            autoComplete='on'
            placeholder='비밀번호'
            v-model='password'
            >
            <button class='inlineToBlock ordinaryLgin unactivatedLoginColor btn btn-primary' type="submit" >로그인</button>
            
            <div>
                <!-- 소셜 로그인 할거라면 넣을곳 -->
            </div>
          </div>
        </form>
          <div class='haveAccount'>
              
              <button @click="goToSignup">회원가입</button>  
              
          </div>  
    </div>
  </nav>
</template>

<script>
export default {
    name: 'LogIn',
    data(){
        return{
            username: null,
            password: null,
        }
    },
    methods:{
      logIn(){
        const username = this.username
        const password = this.password
        // if (password !== this.password){
        //   alert('회원정보가 일치하지 않습니다')
        // }
        const payload = { username, password }
        
        this.$store.dispatch('logIn', payload)
        
        // console.log(payload)
        // this.$router.push({name: 'HomeView', params:{ username: this.username} })
      },
      
      goToSignup() {
        return this.$router.push('/signup')
      }
    }
}
</script>

<style>
@font-face{
  font-family: 'Jua-Regular';
  src:url('/font/Jua-Regular.ttf')
}
.jua{
  font-family: 'Jua-Regular';
  font-size: 50px;
  /* margin: 20px; */
  margin-top: 100px;
  text-align: center;
} 


body {
    background-color: #f9f9f9;
}

.contentsWrap{
    /* position: absolute; */
    padding:1px;
    margin: auto;
    margin-bottom: 10px;
    max-width: 350px;
    border-bottom : 1px;
    /* padding: 50px; */
    /* text-align: center; */
}

.loginWindow {
    margin-top: -10rem;
    /* padding:1px; */
    overflow: hidden;
    background-color: #fcfcfc;
    padding: 10px auto;
    height: 400px;
    border: 1px solid #dfdfdf;
    border-radius: 3px;
}

.loginWindow input{
    /* margin-top : 100px; */
    margin-bottom: 10px;
    background-color: #f5f5f5;
    height: 37px;
    padding: 10px 10px;
    box-sizing: border-box;
    border: 1px solid #eaeaea;
    border-radius: 4px;
}

.loginWindow input::placeholder{
    font-size: 12px;
    font-weight:100;
    text-align: justify;
}

.loginWindow input:focus {
    outline:none;
    border: 1px solid #aaaaaa;
    border-radius: 4px;
}

.ordinaryLogin {
    height: 37px;
    margin-bottom: 10px;
    box-sizing: border-box;
    border: 0px;
    border-radius: 5px;
    color: #ffffff;
    font-size: 15px;
    font-weight: 700;
}

.unactivatedLoginColor {
    background-color: #acd5e8;
}

.activatedLoginColor {
    background-color: #00aeff;
}

.loginWindow * {
    width: 70%;
    margin-left: auto;
    margin-right: auto;
}

#instaLogo {
    margin: 40px auto 30px;
    max-width: 175px;
}

.inlineToBlock {
    display: block;
    margin: 10px;
    font-size: 17px;
}

/*
.horizonAndOr {
    margin:10% 0;
    width:100%;
    box-sizing: border-box;
}
*/
.leftHr {
    float:left;
    width:35%;
    box-sizing: border-box;
}

.or{
    float:left;
    width:17%;
    margin:2px 5%;
    font-size: 13px;
    box-sizing: border-box;

    color: #999999;
    font-size: 14px;
    font-weight: 700;
    margin:0px 15px;
}

.rightHr {
    float: right;
    width:35%;
    box-sizing: border-box;
}

.facebookLogin {
    margin-top: 10px;
    margin-bottom:10px;
    background-color: rgba(255, 255, 255, 0.5);
  
    height: 37px;
    
    box-sizing: border-box;
    border: 0px;
    border-radius: 5px;
    color: #00628f;
    font-size: 15px;
    font-weight: 700;
}

.facebookIcon {
    width:13px;
}


.haveAccount {
    background-color: #fcfcfc;
    margin-top: 10px;
    padding: 15px;
    border: 1px solid #dfdfdf;
    border-radius: 3px;
}

.haveAccount p {
    font-size: 14px;
    font-weight: 300;
    color: #333333;
    
}

.haveAccount div p a{
    font-weight: 600;
    color: #248ae3;
    text-decoration: none;
}

.noneunderline {
    text-decoration:none;
}
body {
    background-color: #f9f9f9;
}

.contentsWrap{
    /* margin: auto; */
    margin-top: 40px;
    max-width: 400px;
    border: none;
    max-height: 200px;
    padding: 20px;
    text-align: center;
}

.loginWindow {
    background-color: #fcfcfc;
    padding: 10px auto;
    border: 1px solid #dfdfdf;
    border-radius: 3px;
}

.loginWindow input{
    margin-bottom: 10px;
    background-color: #f5f5f5;
    height: 37px;
    padding: 10px 10px;
    box-sizing: border-box;
    border: 1px solid #eaeaea;
    border-radius: 4px;
}

.loginWindow input::placeholder{
    font-size: 12px;
    font-weight:100;
}

.loginWindow input:focus {
    outline:none;
    border: 1px solid #aaaaaa;
    border-radius: 4px;
}

.ordinaryLogin {
    height: 37px;
    margin-bottom: 10px;
    box-sizing: border-box;
    border: 0px;
    border-radius: 5px;
    color: #ffffff;
    font-size: 15px;
    font-weight: 700;
}

.unactivatedLoginColor {
    background-color: #acd5e8;
}

.activatedLoginColor {
    background-color: #00aeff;
}

.loginWindow * {
    width: 70%;
    margin-left: auto;
    margin-right: auto;
}

#instaLogo {
    margin: 40px auto 30px;
    max-width: 175px;
}

.inlineToBlock {
    display: block;
}

/*
.horizonAndOr {
    margin:10% 0;
    width:100%;
    box-sizing: border-box;
}
*/
.leftHr {
    float:left;
    width:35%;
    box-sizing: border-box;
}

.or{
    float:left;
    width:17%;
    margin:2px 5%;
    font-size: 13px;
    box-sizing: border-box;

    color: #999999;
    font-size: 14px;
    font-weight: 700;
    margin:0px 15px;
}

.rightHr {
    float: right;
    width:35%;
    box-sizing: border-box;
}

.facebookLogin {
    margin-top: 10px;
    margin-bottom:10px;
    background-color: rgba(255, 255, 255, 0.5);
  
    height: 37px;
    
    box-sizing: border-box;
    border: 0px;
    border-radius: 5px;
    color: #00628f;
    font-size: 15px;
    font-weight: 700;
}

.facebookIcon {
    width:13px;
}


.haveAccount {
    background-color: #fcfcfc;
    margin-top: 10px;
    padding: 15px;
    border: 1px solid #dfdfdf;
    border-radius: 3px;
}

.haveAccount p {
    font-size: 14px;
    font-weight: 300;
    color: #333333;
}

.haveAccount p a{
    font-weight: 600;
    color: #248ae3;
}

.noneunderline {
    text-decoration:none;
}
</style>