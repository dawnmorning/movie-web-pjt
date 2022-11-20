<template>

    <div>
        <h1>회원 가입</h1>
        <form @submit.prevent='signUp'>
            <div>
                <label for="username">*아이디 </label>
                <input type="text" id='username' v-model.trim='username' placeholder="아이디를 입력하세요">
                <p v-if="ErrorMessage?.username">{{ ErrorMessage.username[0] }}</p>
            </div>
            <div>
                <label for="nickname">*닉네임 </label>
                <input type="text" id='nickname' v-model.trim='nickname' placeholder="닉네임을 입력하세요">
                <p v-if="ErrorMessage?.nickname">{{ ErrorMessage.nickname[0] }}</p>
                
            </div>
            <div>
                <label for="email">email </label>
                <input type="text" id='email' v-model.trim='email' placeholder="이메일을 입력하세요">
                <p v-if="ErrorMessage?.email">{{ ErrorMessage.email[0] }}</p>
                
            </div>
            <div>
                <label for="password1">*비밀번호 </label>
                <input type="password" id='password1' v-model.trim='password1' placeholder="비밀번호를 입력하세요">
                <p v-if="ErrorMessage?.password1">{{ ErrorMessage.password1[0] }}</p>
                
            </div>
            <div>
                <label for="password2">*비밀번호 확인 </label>
                <input type="password" id='password2' v-model.trim='password2' placeholder="비밀번호를 입력하세요">
                <p v-if="ErrorMessage?.password2">{{ ErrorMessage.password2[0] }}</p>
                <p v-if="dismatchPW">{{ dismatchPW }}</p>
                
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
                alert("The two password fields didn't match.")
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

</style>