<template>
  <v-speed-dial
    v-model="fab"
    top right absolute
    direction="bottom"
    open-on-hover
    transition="slide-y-reverse-transition"
  >
    <template v-slot:activator>
      <v-btn
        v-model="fab"
        color="secondary"
        dark
        fab
      >
        <v-icon v-if="fab">mdi-close</v-icon>
        <v-icon v-else>mdi-settings</v-icon>
      </v-btn>
    </template>
    <v-btn
      fab
      dark
      small
      color="green"
    >
      <v-icon>mdi-shuffle</v-icon>
    </v-btn>
    <v-btn
      fab
      dark
      small
      color="indigo"
    >
      <v-icon>mdi-plus</v-icon>
    </v-btn>
    <v-btn
      fab
      dark
      small
      color="red"
    >
      <v-icon>mdi-delete</v-icon>
    </v-btn>
  </v-speed-dial>
</template>

<script>
import { mapState, mapGetters, mapMutations } from 'vuex';
export default {
  data () {
    return {
      fab: false,
    }
  },
  computed: {
    ...mapState(['room', 'game', 'connected']),
    ...mapGetters(['gameWon']),
    isFirstTurn() {
        if (!this.connected) {
          return true;
        }
        if (this.game.board) {
          return Object.values(this.game.board).every(e => e === false);
        }
        return true;
      },
  },
  methods: {
    ...mapMutations(['reset_room']),
    newGame(reset) {
      // reset spymaster state and go to player view
      // emit message to start a new game
      const params = {
        room: this.room,
      };
      if (reset === true) {
        this.reset_room()
        params['newGame'] = true
        this.$router.push({ path: `/${this.room}/player` })
      }
      this.$socket.emit('regenerate', params);
    },
  }
}
</script>
