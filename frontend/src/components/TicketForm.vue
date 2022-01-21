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
import APIHandler from '@/services/api'
import Storage from '@/services/storage'

/*eslint-disable*/
export default {
    data() {
        return {
            price: "",
            sessionFriday: 0,
            sessionSaturday: 0,
            sessionSunday: 0, 
            apiClient: null
        }
    },
    methods: {
        handleAddTicket(e) {
            e.preventDefault();

            const session = this.sessionFriday | this.sessionSaturday | this.sessionSunday;

            this.apiClient.addTicket(this.price, session, this.$route.params.gpId)
                .then(() => {
                    this.$router.push(`/tickets/${this.$route.params.gpId}`);
                })
                .catch((error) => {
                    alert(error);
                    console.error(`ERROR while adding ticket: ${error}`);
                });
        },
        goBack() {
            this.$router.push(`/tickets/${this.$route.params.gpId}`);
        }
    },
    created() {
        const storage = new Storage(window.localStorage);

        if (storage.get('role') !== 'vendor') {
            this.$router.push('/gps');
        }

        this.apiClient = new APIHandler();
    }
}
</script>
