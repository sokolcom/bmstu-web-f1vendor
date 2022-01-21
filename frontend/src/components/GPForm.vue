<template>
    <figure class="container">
        <h1 class="h">New GRAND PRIX</h1>
        <form>
            <label for="name">GP title</label>
            <div>
                <input type="username" v-model="gpTitle" required autofocus>
            </div>
            <div>
                <label for="date">Date</label>
                <div>
                    <input type="date" v-model="gpDate" required>
                </div>
            </div>
            <div>
                <button type="submit" @click="handleAddGP">
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
        const today = new Date();
        const todayDate = 
            today.getFullYear() + '-' + 
            ('0' + (today.getMonth() + 1)).slice(-2) + '-' + 
            ('0' + today.getDate()).slice(-2);
        return {
            id: "",
            gpTitle: "",
            gpDate: todayDate, 
            apiClient: null
        }
    },
    methods: {
        handleAddGP(e) {
            e.preventDefault();

            this.apiClient.addGP(this.gpTitle, this.gpDate, this.id)
                .then(() => {
                    this.$router.push('/gps');
                })
                .catch((error) => {
                    alert(error);
                    console.error(`ERROR while adding GP: ${error}`);
                });
        },
        goBack() {
            this.$router.push('/gps');
        }
    },
    created() {
        const storage = new Storage(window.localStorage);

        if (storage.get('role') !== 'vendor') {
            this.$router.push('/gps');
        }
        this.id = storage.get('id');
        this.apiClient = new APIHandler();
    }
}
</script>
