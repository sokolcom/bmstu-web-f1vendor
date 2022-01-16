<template>
  <figure class="running-text">
    <p class="marquee">
      <span>BUY F1 TICKETS BUY F1 TICKETS BUY F1 TICKETS BUY F1 TICKETS BUY F1 TICKETS BUY F1 TICKETS&nbsp;</span>
    </p>
    <p class="marquee marquee2">
      <span>BUY F1 TICKETS BUY F1 TICKETS BUY F1 TICKETS BUY F1 TICKETS BUY F1 TICKETS BUY F1 TICKETS&nbsp;</span>
    </p>
  </figure>
  <figure class="meme-placeholder">
    <img alt="Capitalism meme" src="../assets/capitalism.webp">
  </figure>
</template>

<style>

html {
  overflow-x: hidden;
}

.running-text {
  font-size: 35px;
  font-family: "Formula1 Display-Regular";
  color: #ff1801;
}

.marquee {
  margin: 0 auto;
  white-space: nowrap;
  overflow: hidden;
  position: absolute;
}

.marquee span {
  display: inline-block;
  padding-left: 100%;
  animation: marquee 20s linear infinite;
}

.marquee2 span {
  animation-delay: 10s;
}

@keyframes marquee {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(-100%, 0);
  }
}
img {
  display: block;
  margin-top: 100px;
  margin-left: auto;
  margin-right: auto;
  height: 600px;
}
</style>
