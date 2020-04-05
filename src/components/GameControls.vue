<template>
  <div>
    <v-btn fab top right absolute small class="pa-2" v-if="gameWon" color="success" @click.native="newGame(true)">
      <v-icon>autorenew</v-icon>
    </v-btn>
    <v-btn fab top right absolute small class="pa-2" v-if="isFirstTurn && !gameWon" color="success" @click.native="newGame" id="shuffle-btn">
      <v-icon>shuffle</v-icon>
    </v-btn>
  </div>
</template>

<script>
import { mapState, mapGetters, mapMutations } from 'vuex';
export default {
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
