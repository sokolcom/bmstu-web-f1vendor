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
import axios from 'axios'

/*eslint-disable*/
export default {
    data() {
        const today = new Date();
        const todayDate = 
            today.getFullYear() + '-' + 
            ('0' + (today.getMonth() + 1)).slice(-2) + '-' + 
            ('0' + today.getDate()).slice(-2);
        return {
            gpTitle: "",
            gpDate: todayDate
        }
    },
    methods: {
        handleAddGP(e) {
            e.preventDefault();
            if (this.gpTitle.length > 0) {
                const path = 'http://localhost:8888/api/v1/grands-prix';
                const token = localStorage.getItem('token');
                const userId = localStorage.getItem('id');
                axios.post(path, {
                    "title": this.gpTitle,
                    "date": this.gpDate,
                    "vendor_id": userId
                }, {
                    headers: {
                        'Authorization': token
                    }
                })
                    .then((res) => {
                        this.$router.push('/gps');
                    })
                    .catch((error) => {
                        console.error(`ERROR while adding GP: ${error}`);
                    });
            } else {
                alert("GP title is missing!\nAdd one and try again!");
            }
        },
        goBack() {
            this.$router.push('/gps');
        },
        created() {
            if (localStorage.getItem('id') === 'client') {
                this.$router.push('/gps');
            }
        }
    }
}
</script>
