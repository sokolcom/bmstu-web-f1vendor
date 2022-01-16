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
import axios from 'axios'
/* eslint-disable */
export default {
    props : ["nextUrl"],
    data(){
        return {
            username : "",
            password : "",
            passwordConfirmation : "",
            role : ""
        }
    },
    methods : {
        handleSignUp(e) {
             e.preventDefault();
            if (this.username.length == 0) {
                this.password = "";
                this.passwordConfirmation = "";
                return alert("Username's missing!\nTry again!");
            }
            if (this.role.length == 0) {
                this.password = "";
                this.passwordConfirmation = "";
                return alert("Role's missing!\nTry again!");
            }
            if ((this.password.length > 0) && (this.password === this.passwordConfirmation))
            {
                let url = "http://localhost:8888/api/v1/users"
                console.log(this.username, this.password, this.role);
                axios.post(url, {
                    username: this.username,
                    password: this.password,
                    role: this.role
                })
                    .then(response => {
                        console.log(response.data);
                        let data = response.data.result;
                        localStorage.setItem('token', data.token);
                        localStorage.setItem('role', data.role);
                        localStorage.setItem('id', data.id);

                        (this.$route.params.nextUrl != null) ? 
                            this.$router.push(this.$route.params.nextUrl) :
                            this.$router.push('/gps');
                    })
                    .catch((error) => {
                        alert(`Registration FAILED!\n${error}`);
                        console.error(`ERROR while retrieving data: ${error}`);
                    });
            } else {
                this.password = "";
                this.passwordConfirmation = "";
                return alert("Passwords do not match!\nTry again!");
            }
        }
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
