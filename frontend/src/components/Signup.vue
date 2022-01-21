<template>
    <article class="article-signup">
        <h3>Sign Up</h3>
        <form class="form-signup">
            <label for="username">Userame</label>
            <div>
                <input id="username" type="text" v-model="username" required autofocus>
            </div>

            <label for="password">Password</label>
            <div>
                <input id="password" type="password" v-model="password" required>
            </div>

            <label for="password-confirm">Confirm password</label>
            <div>
                <input id="password-confirm" type="password"
                v-model="passwordConfirmation" required>
            </div>
            <div class="role-radio">
                <div>
                    <input class="radio-input" name="role" type="radio" value="client" v-model="role">
                    <label>User</label>
                </div>
                <div>
                    <input class="radio-input" name="role" type="radio" value="vendor" v-model="role">
                    <label>Vendor</label>
                </div>
                <br>
            </div>
            <div>
                <button type="submit" @click="handleSignUp">
                    Sign Up
                </button>
            </div>
        </form>
    </article>
</template>

<script>
import APIHandler from '@/services/api'
/* eslint-disable */
export default {
    props : ["nextUrl"],
    data(){
        return {
            username : "",
            password : "",
            passwordConfirmation : "",
            role : "", 
            apiClient: null
        }
    },
    methods : {
        handleSignUp(e) {
            e.preventDefault();
            
            this.apiClient.signup(this.username, this.password, this.passwordConfirmation, this.role)
                .then(() => 
                    (this.$route.params.nextUrl != null) ? 
                        this.$router.push(this.$route.params.nextUrl) :
                        this.$router.push('/gps')
                )
                .catch((error) => {
                    this.password = "";
                    this.passwordConfirmation = "";
                    alert(`Registration FAILED!\n${error}`);
                    console.error(`ERROR while retrieving data: ${error}`);
                });
        }
    }, 
    created() {
        this.apiClient = new APIHandler();
    }
}
</script> 

<style>

.article-signup {
	background-color: #D3D3D3;
    border: 2px solid #222;
    width: 300px;
    height: 480px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
	align-items: center;
	margin-left: auto;
    margin-right: auto;
	vertical-align: middle;
                 
	font-family: "Formula1 Display-Regular";
    border-radius: 10px; 
	margin: 70px auto auto auto;
}

h3 {
    text-align: center;
}

button  {
	width: 100%;
  	margin: 4px;
	position: relative;
	border-radius: 20px;
	border: 1px solid #222;
	background-color: #222;
	color: #FFFFFF !important;
	font-size: 12px;
	font-weight: bold;
	padding: 12px 45px;
	letter-spacing: 1px;
	text-transform: uppercase;
	transition: transform 80ms ease-in;
    margin-top: 10px !important;
}

button:active {
	transform: scale(0.95);
}

button:focus {
	outline: none;
}

button.ghost {
	background-color: transparent;
	border-color: #FFFFFF;
}

.form-signup {
	background-color: #D3D3D3;
	display: flex;
	align-items: center;
	justify-content: baseline;
	flex-direction: column;
	padding: 50px 0 0 0;
    height: 500px;
	text-align: center;
}

label {
    margin-top: 0 !important;
    margin-bottom: 10px !important;
}

input {
	background-color: #eee;
	border: none;
	padding: 12px 15px;
	width: 100%;
    margin-top: 0 !important;
    margin-bottom: 10px !important;
}

.role-radio {
    display: flex !important;
    flex-direction: row !important;
    justify-content: space-around !important;
}

.radio-input {
    padding: 10px;
}

footer {
    bottom: 0;
    position: fixed;
    left: 0;
    right: 0;
    text-align: center;
    z-index: 999;
}
</style>
