<template>
    <article  class="article-login">
        <h3>Sign In</h3>
        <form class="form-login">
            <label for="email">Username</label>
            <div>
                <input type="username" v-model="username" required autofocus>
            </div>
            <div>
                <label for="password">Password</label>
                <div>
                    <input  type="password" v-model="password" required>
                </div>
            </div>
            <div>
                <button type="submit" @click="handleSignIn">
                    Sign In
                </button>
            </div>
        </form>
    </article>
</template>

<script>
import axios from 'axios'
/* eslint-disable */
export default {    
    data() {
        return {
            username: "",
            password: ""
        }
    },
    methods: {
        handleSignIn(e) {
            e.preventDefault()
            axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
            if (this.password.length > 0) {
                axios.post('http://localhost:8888/api/v1/users/login', {
                    username: this.username,
                    password: this.password
                },
                { headers: {}, useCredentails: true })
                .then(response => {
                    console.log(response.data.result);
                    let data = response.data.result;
                    localStorage.clear();
                    localStorage.setItem('token', data.token);
                    localStorage.setItem('role', data.role);
                    localStorage.setItem('id', data.id);
                    this.$router.push('/gps');
                })
                .catch(function (error) {
                    alert(`Authorization FAILED!\n${error}`);
                    console.error(error.response);
                });
            }
        }
    }  
}
</script>

<style>

.article-login {
	background-color: #D3D3D3;
    border: 2px solid #222;
    width: 300px;
    height: 350px;
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

.form-login {
	background-color: #D3D3D3;
	display: flex;
	align-items: center;
	justify-content: baseline;
	flex-direction: column;
	padding: 50px 0 0 0;
    height: 283px;
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

footer {
    bottom: 0;
    position: fixed;
    left: 0;
    right: 0;
    text-align: center;
    z-index: 999;
}

</style>
