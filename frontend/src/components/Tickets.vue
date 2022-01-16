<template>
    <div class="tickets-container">
        <div class="grid-cell" v-for="(ticket, index) in tickets" :key="index">
            <p class="is-availible">{{ ticket.in_stock ? "IN STOCK" : "SOLD OUT" }}</p>
            <p class="price">{{ ticket.price }}$</p>
            <p class="session">Session: {{ decodeSession(ticket.session).toUpperCase() }}</p>
            <p class="vendor">Vendor: {{ ticket.vendor_name.toUpperCase() }}</p>
            <div class="button-handle">
                <button v-if="this.role === 'client'" :disabled="ticket.in_stock === false"
                @click="buyTicket(ticket.id)">
                    Buy
                </button>
                <button v-if="this.role === 'vendor'" @click="deleteTicket(ticket.id)">
                    Delete
                </button>
            </div>
        </div>
        <div class="grid-cell add" v-if="this.role === 'vendor'"
        @click="addTicket">
            <p class="add-ticket">+</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

/* eslint-disable */
export default {
  data() {
    return {
      tickets: [],
      role: null
    };
  },
  methods: {
    goBack() {
      this.$router.push('/gps');
    },
    decodeSession(sessionCode) {
      const days = ["Friday" ," Saturday", "Sunday"];
      let result = "";
      let idx = 2;
      while (idx > -1) {
          if (sessionCode & 1) {
            result = days[idx] + '-' + result;
          }
          sessionCode >>= 1;
          idx -= 1;
      }
      return result.replace(/^\-+|\-+$/g, '');
    },
    buyTicket(ticketId) {
      const path = 'http://localhost:8888/api/v1/tickets/buy';
      let token = localStorage.getItem('token');
      axios.patch(path,
        {
          'ticket_id': ticketId,
        }, {
          headers: {
          'Authorization': token
        }
      })
        .then((res) => {
          console.log(res);
          alert("CONGRATS!!!\nTicket is yours!!!!!!!");
          this.fetchTickets();
        })
        .catch((error) => {
          console.error(`ERROR while processing purchase: ${error}`);
        });
    },
    addTicket() {
        // this.$router.push(`/tickets/add`);
        this.$router.push({ name: `TicketForm`, params: { gpId: this.$route.params.gp_id } });
    },
    deleteTicket(ticketId) {
      const path = `http://localhost:8888/api/v1/tickets/${ticketId}`;
      let token = localStorage.getItem('token');
      axios.delete(path, {
          headers: {
          'Authorization': token
        }
      })
        .then((res) => {
          console.log(res);
          this.fetchTickets();
        })
        .catch((error) => {
          console.error(`ERROR while processing ticket: ${error}`);
        }); 
    },
    fetchTickets() {
      const path = `http://localhost:8888/api/v1/tickets/${this.$route.params.gp_id}`;
      let token = localStorage.getItem('token');
      axios.get(path, {
        headers: {
          'Authorization': token
        }
      })
        .then((res) => {
          this.tickets = res.data.result;
        })
        .catch((error) => {
          localStorage.clear();
          this.$router.push('/login');
          console.error(`ERROR while retrieving data: ${error}`);
        });
    }
  },
  created() {
    this.role = localStorage.getItem('role');
    this.fetchTickets();
  }
}
</script>

<style>
.tickets-container {
    display: grid; 
    grid-auto-columns: 1fr 1fr; 
    grid-auto-rows: 1fr 1fr; 
    grid-template-columns: 25% 25% 25%; 
    grid-template-rows: 1fr 1fr 1fr; 
    gap: 10px 10px; 
    grid-template-areas: 
        ". . ."
        ". . ."
        ". . ."; 
    justify-content: center; 
    align-content: start; 
    justify-items: center; 
    align-items: start;

    font-family: "Formula1 Display-Regular";
    padding-top: 50px;
}
.grid-cell {
    border: 2px solid #222;
    border-radius: 10px;
    background-color: #D3D3D3;
    padding: 5px;
}
.add {
    background-color: white;
    border: 2px dashed #222;
    border-radius: 10px;
    padding: 50px;
    font-size: 70px;
    text-align: center !important;
}
.is-availible {
    text-align: center !important;
}
.price {
    font-size: 25px;
}
.button-handle {
    padding: 10px;
}
button:disabled {
    background-color: #888;
    border-color: #888;
    transform: none !important;
}

</style>
