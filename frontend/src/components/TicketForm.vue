<template>
    <figure class="container">
        <h1 class="h">New TICKET</h1>
        <form>
            <label for="name">Price</label>
            <div>
                <input type="price" v-model="price" required autofocus>
            </div>
            <div>
                <label for="session">Session</label>
                <div class="role-radio">
                <div>
                    <input class="radio-input" type="radio" value=4 v-model="sessionFriday">
                    <label>Friday</label>
                </div>
                <div>
                    <input class="radio-input" type="radio" value=2 v-model="sessionSaturday">
                    <label>Saturday</label>
                </div>
                <div>
                    <input class="radio-input" type="radio" value=1 v-model="sessionSunday">
                    <label>Sunday</label>
                </div>
            </div>
            </div>
            <div>
                <button type="submit" @click="handleAddTicket">
                    Add
                </button>
            </div>
            <div>
                <button @click="goBack()">
                    Back
                </button>
            </div>
        </form>
    </figure>
</template>

<script>
import axios from 'axios'

/*eslint-disable*/
export default {
    data() {
        return {
            price: "",
            sessionFriday: 0,
            sessionSaturday: 0,
            sessionSunday: 0
        }
    },
    methods: {
        handleAddTicket(e) {
            e.preventDefault();
            const session = this.sessionFriday | this.sessionSaturday | this.sessionSunday;
            if ((this.price > 0) && (session !== 0)) {
                const path = 'http://localhost:8888/api/v1/tickets';
                const token = localStorage.getItem('token');
                const gpId = this.$route.params.gpId;
                axios.post(path, {
                    "price": this.price,
                    "session": session,
                    "gp_id": gpId
                }, {
                    headers: {
                        'Authorization': token
                    }
                })
                    .then((res) => {
                        this.$router.push(`/tickets/${this.$route.params.gpId}`);
                    })
                    .catch((error) => {
                        console.error(`ERROR while adding ticket: ${error}`);
                    });
            } else {
                alert("Some information is missing!\nFill price & session and try again!");
            }
        },
        goBack() {
            this.$router.push(`/tickets/${this.$route.params.gpId}`);
        },
        created() {
            if (localStorage.getItem('id') === 'client') {
                this.$router.push('/gps');
            }
        }
    }
}
</script>
