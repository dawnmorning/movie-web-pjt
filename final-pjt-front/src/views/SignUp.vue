<template>
    <div>
        <h1>회원 가입</h1>
        <form @submit.prevent='signUp'>
            <div>
                <label for="username">아이디 </label>
                <input type="text" id='username' v-model='username' placeholder="아이디를 입력하세요">
            </div>
            <div>
                <label for="password1">비밀번호 </label>
                <input type="password" id='password1' v-model='password1' placeholder="비밀번호를 입력하세요">
            </div>
            <div>
                <label for="password2">비밀번호 확인 </label>
                <input type="password" id='password2' v-model='password2' placeholder="비밀번호를 입력하세요">
            </div>
            <input type="submit" value='Signup'>
            <!-- <button>뒤로 가기</button> -->
        </form>
    </div>
</template>

<script>

// const DJ_URL = 'http::/'

export default {
    name: 'SignUp',
    data(){
        return{
            username: null,
            password1: null,
            password2: null,
            email:null,
        }
    },
    methods:{
        signUp(){
            const username = this.username
            const password1 = this.password1
            const password2 = this.password2
            const email = this.email

            const payload={
                username, password1, password2, email
            }

            this.$store.dispatch('signUp', payload)
            if (this.username && this.password1 && this.password2){
                this.$router.push('/')
            }  else {
                alert('빈 곳이 있어서는 안 돼요 ㅠㅠ')
            }
        }
    }
}
</script>

<style>

</style>