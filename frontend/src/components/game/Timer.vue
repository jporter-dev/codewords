<template>
  <v-speed-dial
    v-model="fab"
    direction="bottom"
    transition="slide-y-transition"
  >
    <template v-slot:activator>
      <v-btn
        dark
        outlined
        class="timer"
        :class="{flash: timesUp}"
      >
        {{minutes}}:{{seconds}}
      </v-btn>
    </template>
    <v-tooltip right>
      <template v-slot:activator="{ on }">
        <v-btn
          fab
          dark
          small
          color="green"
          v-on="on"
          @click="start"
        >
          <v-icon>mdi-play</v-icon>
        </v-btn>
      </template>
      <span>Start Timer</span>
    </v-tooltip>
    <v-tooltip right>
      <template v-slot:activator="{ on }">
        <v-btn
          fab
          dark
          small
          color="red darken-2"
          v-on="on"
          @click="reset"
        >
          <v-icon>mdi-restart</v-icon>
        </v-btn>
      </template>
      <span>Reset Timer</span>
    </v-tooltip>
  </v-speed-dial>
</template>

<script>
let tickTime = 1000 * 60 * 3;
export default {
  data() {
    return {
      fab: false,
      tick: tickTime,
      interval: null
    };
  },
  computed: {
    minutes() {
      return Math.floor((this.tick % (1000 * 60 * 60)) / (1000 * 60));
    },
    seconds() {
      let t = Math.floor((this.tick % (1000 * 60)) / 1000);
      return t < 10 ? `0${t}` : t;
    },
    timesUp() {
      return this.tick === 0;
    }
  },
  sockets: {
    startTimer() {
      this.interval = setInterval(() => {
        if (this.tick > 0) this.tick -= 1000;
        else clearInterval(this.interval);
      }, 1000);
    },
    resetTimer() {
      clearInterval(this.interval);
      this.tick = tickTime; // 3 minutes
    }
  },
  methods: {
    start() {
      this.$socket.emit("start_timer", { room: this.$store.state.room });
    },
    reset() {
      this.$socket.emit("reset_timer", { room: this.$store.state.room });
    }
  }
};
</script>

<style lang="scss" scoped>
@-webkit-keyframes flash {
  0% {
    background-color: white;
  }
  100% {
    background-color: transparent;
  }
}

.flash {
  -webkit-animation: flash 1s ease-out infinite;
  animation: flash 1s ease-out infinite;
}
</style>
