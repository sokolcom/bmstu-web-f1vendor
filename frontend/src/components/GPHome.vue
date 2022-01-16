<template>
  <figure class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>GPs</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Grand Prix</th>
              <th scope="col">Date</th>
            </tr>
          </thead>
          <tbody>
            <tr class="table-content" v-for="(gp, index) in gps" :key="index"
            >
              <td type="name" @click="goToTickets(gp.id)">{{ gp.title }}</td>
              <td type="date" @click="goToTickets(gp.id)">{{ new Date(gp.date).toDateString() }}</td>
              <td type="name" v-if="this.role === 'vendor'">
                <button class="delete-gp" @click="deleteGP(gp.id)">-</button>
              </td>
            </tr>
          </tbody>
        </table>
        <button v-if="this.role === 'vendor'" v-on:click="this.addGP()">Add GP</button>
      </div>
    </div>
  </figure>
</template>

<script>
import axios from 'axios'

/* eslint-disable */
export default {
  data() {
    return {
      gps: [],
      role: null
    };
  },
  methods: {
    goToTickets(id) {
      this.$router.push(`/tickets/${id}`);
    },
    addGP() {
      this.$router.push('/gps/add');
    },
    deleteGP(gpId) {
      const path = `http://localhost:8888/api/v1/grands-prix/${gpId}`;
      let token = localStorage.getItem('token');
      axios.delete(path, {
        headers: {
          'Authorization': token
        }
      })
        .then((res) => {
          this.fetchGPs();
        })
        .catch((error) => {
          console.error(`ERROR while deleting GP: ${error}`);
        });
    },
    fetchGPs() {
      const path = 'http://localhost:8888/api/v1/grands-prix';
      let token = localStorage.getItem('token');
      axios.get(path, {
        headers: {
          'Authorization': token
        }
      })
        .then((res) => {
          this.gps = res.data.result;
          if (this.role === 'vendor') {
            this.gps = this.gps.filter(item => (item.vendor_id == this.id));
          }
        })
        .catch((error) => {
          this.$router.push('/login');
          console.error(`ERROR while retrieving data: ${error}`);
        });
    }
  },
  created() {
    this.id = localStorage.getItem('id');
    this.role = localStorage.getItem('role');
    this.fetchGPs();
  }
}
</script>

<style>
.container {
	margin: 70px auto auto auto;
  font-family: "Formula1 Display-Regular";   
}
.table-content {
    color: #222;
    text-decoration: none;

}
.table-content:hover {
    color: #3c97bf;
    text-decoration: none;
}
.delete-gp {
  height: 25px;
  line-height: 25px;  
  width: 25px;  
  font-size: 2em;
  font-weight: bold;
  border-radius: 50%;
  background-color: #222;
  color: white;
  text-align: center;
  padding: 0;
  cursor: pointer;
}
</style>
