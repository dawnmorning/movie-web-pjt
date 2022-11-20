<template>
  <nav class='navWrap'>
    <div class='contentsWrap ' style='font-size:20px; margin-top:0;'>
        <form @submit.prevent='signUp' class = 'formWrap animate__animated animate__fadeIn'>
            <!-- <div class="jua"></div> -->
            <div class='signupWindow jua' style=''>
                <h1>회원 가입</h1>
                <div class="inlineToBlock">
                    <input type="text" id='username' v-model.trim='username' placeholder="아이디" class='id'>
                    <p class='ErrorMsg' v-if="ErrorMessage?.username">{{ ErrorMessage.username[0] }}</p>
                </div>
                <div class="inlineToBlock">
                    <input type="text" id='nickname' v-model.trim='nickname' placeholder="닉네임" class='nickname'>
                    <p class='ErrorMsg' v-if="ErrorMessage?.nickname">{{ ErrorMessage.nickname[0] }}</p>         
                </div>
                <div class="inlineToBlock">
                    <input type="text" id='email' v-model.trim='email' placeholder="이메일" class='email'>
                    <p class='ErrorMsg' v-if="ErrorMessage?.email">{{ ErrorMessage.email[0] }}</p>
                    
                </div>
                <div class="inlineToBlock">
                    <input type="password" id='password1' v-model.trim='password1' placeholder="비밀번호" class='pw'>
                    <p class='ErrorMsg' v-if="ErrorMessage?.password1">{{ ErrorMessage.password1[0] }}</p>
                    
                </div>
                <div class="inlineToBlock">
                    <input type="password" id='password2' v-model.trim='password2' placeholder="비밀번호 확인" class='pw'>
                    <div>
                        <p class='ErrorMsg' v-if="ErrorMessage?.password2" style= 'margin-bottom: 0px;'>{{ ErrorMessage.password2[0] }}</p>
                        <p class='ErrorMsg' v-if="dismatchPW">비밀번호가 동일하지 않습니다.</p>
                    </div>
                    
                </div>
                <button class='inlineToBlock ordinaryLgin unactivatedLoginColor btn btn-primary' type="submit" style='margin-top:0'>회원가입</button>
                <!-- <button>뒤로 가기</button> -->

            </div>
        </form>
    </div>
      
  </nav>
</template>
<script>

// const DJ_URL = 'http::/'

export default {
    name: 'SignUp',
    data(){
        return{
            username: null,
            nickname: null,
            email:null,
            password1: null,
            password2: null,
            
        }
    },
    computed: {
        ErrorMessage() { return this.$route.query.response?.data },
        dismatchPW() { 
            let message = null
            if (this.password1 != this.password2){
                message = "The two password fields didn't match."
            }
            return message
        },

    },
    methods:{
        signUp(){
            this.SignUpError = null
            const username = this.username
            const nickname = this.nickname
            const email = this.email
            const password1 = this.password1
            const password2 = this.password2

            const payload={
                username, nickname, email, password1, password2, 
            }
            if (password1 && password2 && password1 != password2) {
                alert("비밀번호가 일치하지 않습니다")
                this.password1 = this.password2 = null
            }
            else {
                this.$store.dispatch('signUp', payload)
            }

            // if (this.username && this.password1 && this.password2 && this.nickname){
            //     this.$router.push('/')
            // }  
            // else {
            //     alert('빈 곳이 있어서는 안 돼요 ㅠㅠ')
            // }
        }
    }
}
</script>

<style>
@font-face{
  font-family: 'Jua-Regular';
  src:url('/font/Jua-Regular.ttf')
}
p + .ErrorMsg{
    font-size:10px;
}
.navWrap{
    height:0; 
}

.jua{
  font-family: 'Jua-Regular';
  font-size: 50px;
  /* margin: 20px; */
  margin-top: 100px;
  text-align: center;
} 


div .ErrorMsg{
    font-size:13px;
    font-weight: 100;
}


body {
    background-color: #f9f9f9;
    height: 1000px;
}

div h1{
    margin-top: 60px;
    margin-bottom: 30px;
}

.contentsWrap{
    /* position: absolute; */
    /* padding:1px; */
    margin: auto;
    /* margin-bottom: 10px; */
    max-width: 350px;
    /* border-bottom : 1px; */
    /* padding: 50px; */
    /* text-align: center; */
    height: 100px;
}

div .signupWindow {
    margin-top: 5%;
    /* padding:1px; */
    overflow: hidden;
    background-color: #fcfcfc;
    padding: 10px auto;
    height: 650px;
    width: 450px;
    justify-content: center;
    border: 1px solid #dfdfdf;
    border-radius: 3px;
}

.signupWindow input{
    /* margin-top : 100px; */
    margin-bottom: 10px;
    background-color: #f5f5f5;
    height: 37px;
    padding: 10px 10px;
    box-sizing: border-box;
    border: 1px solid #eaeaea;
    border-radius: 4px;
    width: 80%;
}

.signupWindow input::placeholder{
    font-size: 12px;
    font-weight:100;
    text-align: justify;
}

.signupWindow input:focus {
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
    margin: 30px;
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