<template>
  <header id="app">
    <nav id="nav-left">
      <a href="/">F1 Tickets</a>
      <a href="/gps">Grand Prix</a>
    </nav>
    <nav id="nav-right">
      <a v-if="this.token == null && this.role == null" href="/login">Sign In</a>
      <a v-if="this.token == null && this.role == null" href="/signup">Sign Up</a>
      <a v-if="this.token != null && this.role != null" v-on:click="logout()" href="/login" >Log out</a>
    </nav>
  </header>
  <router-view/>
  <footer>
  </footer>
</template>

<script>
/* eslint-disable */
export default {
  name: 'App',
  data() {
    return {
      token: null,
      role: null
    };
  },
  methods: {
      logout() {
          localStorage.removeItem('token');
          localStorage.removeItem('role');
          localStorage.removeItem('id');
      }
    },
  created() {
    this.token = localStorage.getItem('token');
    this.role = localStorage.getItem('role');
  },
  watch: {
    $route (to, from) {
      this.token = localStorage.getItem('token');
      this.role = localStorage.getItem('role');
    }
  }
}
</script>
<style>
html, body { margin: 0 !important; }
@font-face {
  font-family: "Formula1 Display-Regular";
  src: url("//db.onlinewebfonts.com/t/7a45cffcf1eee0797d566deb425ebaa9.eot");
  src:
    url("//db.onlinewebfonts.com/t/7a45cffcf1eee0797d566deb425ebaa9.eot?#iefix") format("embedded-opentype"),
    url("//db.onlinewebfonts.com/t/7a45cffcf1eee0797d566deb425ebaa9.woff2") format("woff2"),
    url("//db.onlinewebfonts.com/t/7a45cffcf1eee0797d566deb425ebaa9.woff") format("woff"),
    url("//db.onlinewebfonts.com/t/7a45cffcf1eee0797d566deb425ebaa9.ttf") format("truetype"),
    url("//db.onlinewebfonts.com/t/7a45cffcf1eee0797d566deb425ebaa9.svg#Formula1 Display-Regular") format("svg");
}
header, footer {
  background-color: #ff1801 !important;
  overflow: hidden;
  font-family: "Formula1 Display-Regular";
}
footer {
  height: 60px;
}
/* Style the links inside the navigation bar */
nav a {
  margin: 0px;
  background-color: #ff1801;
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}
#nav-left {
  float: left;
}
#nav-right {
  float: right;
}
/* Change the color of links on hover */
nav a:hover {
  background-color: #222;
  color: white;
}
</style>
