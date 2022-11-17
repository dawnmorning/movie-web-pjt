<template>
    <section id="container">
      <div id='main_container'>
        <div class='form_container'>
          <div class='input-wrapper'>
            <h1></h1>
            <h1>로그인</h1>
            <form @submit.prevent='logIn'>
              <p class='login-wrapper flex-center'>
                
                <input type="text" id='username' v-model='username'
                class='login-input'
                placeholder='아이디'
                >
              </p>
        
              
              <p class='login-wrapper flex-center'>
                
                <input class= 'login-input' type="password" id='password' 
                placeholder='비밀번호'
                v-model='password'>
              </p>
              <div class='flex-center button-wrapper'>
                <input class='login-button' type="submit" value='logIn'> 

              </div>
        
            </form>
          </div>
        </div>
      </div>

      <div class='flex-center findpass'>
        <div>
          <span>계정이 없다면</span> <a href="http://localhost:8080/signup">이곳으로</a>  
        </div>
      </div>
    </section>
    
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
        const payload = {
          username: username,
          password: password,
        }
        
        this.$store.dispatch('logIn',payload)
        
        // console.log(payload)
        this.$router.push({name: 'HomeView', params:{ username: this.username} })
      }
    }
}
</script>

<style>


body {
  background-color: rgba(var(--b3f, 250, 250, 250), 1);
  height: 100%;
}
.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
.login-container {
  background-color: white;
  width: 380px;
  height: 500px;
  border: 1px solid lightgray;
}
.logo-text {
  font-family: "Lobster", cursive;
  font-size: 55px;
  margin-top: 50px;
}
.input-wrapper {
  margin-top: 60px;
}
.login-wrapper {
  margin-left: 40px;
  margin-right: 40px;
  margin-bottom: 5px;
}
.login-input {
  font-size: 14px;
  width: 330px;
  height: 40px;
  background-color: rgba(0, 0, 0, 0.035);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 5px;
  padding-left: 10px;
}
.login-button {
  width: 100%;
  font-size: 15px;
  color: white;
  font-weight: bold;
  background-color: blue;
  background-color: rgba(0, 162, 255, 0.3);
  border: none;
  border-radius: 5px;
  padding: 9px;
}
.button-wrapper {
  border: none;
  margin: 15px 40px;
}
.findpass {
  margin-top: 140px;
  font-size: 13px;
  color: rgb(86, 96, 235);
}
</style>