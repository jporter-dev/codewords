<template>
  <div v-if="game && game.board">
    <div v-if="isSpymaster">
      <v-speed-dial
        v-model="fab"
        top
        right
        fixed
        open-on-hover
        direction="bottom"
        transition="slide-y-reverse-transition"
      >
        <template v-slot:activator>
          <v-btn
            color="secondary"
            small
            dark
            fab
          >
            <v-icon v-if="fab">mdi-close</v-icon>
            <v-icon v-else>mdi-settings</v-icon>
          </v-btn>
        </template>
        <v-tooltip left>
          <template v-slot:activator="{ on }">
            <v-btn
              fab
              dark
              small
              color="primary"
              v-on="on"
              @click.native="newGame(true)"
            >
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </template>
          <span>New Game</span>
        </v-tooltip>
        <v-tooltip left>
          <template v-slot:activator="{ on }">
            <v-btn
              fab
              dark
              small
              color="green"
              v-on="on"
              @click.native="newGame"
            >
              <v-icon>mdi-shuffle</v-icon>
            </v-btn>
          </template>
          <span>Regenerate Board</span>
        </v-tooltip>
        <v-tooltip left>
          <template v-slot:activator="{ on }">
            <v-btn
              fab
              dark
              small
              color="red darken-2"
              v-on="on"
              @click="closeRoom()"
            >
              <v-icon>mdi-door-closed</v-icon>
            </v-btn>
          </template>
          <span>Close Room</span>
        </v-tooltip>
      </v-speed-dial>
    </div>
    <v-dialog
      v-model="gameWon"
      max-width="350"
      persistent
    >
      <v-card
        color="secondary"
        class="telegram"
      >
        <v-card-title class="justify-center">Game Over!</v-card-title>
        <v-card-title class="justify-center">
          Cards remaining:<scoreboard class="ml-2"></scoreboard>
        </v-card-title>
        <v-card-text v-if="isSpymaster">Start a new game with current game settings or create a new lobby.</v-card-text>
        <v-card-text v-else>Wait for a Spymaster to start a new game or return to the home screen.</v-card-text>
        <v-card-actions class="justify-center">
          <v-btn
            color="primary"
            @click="newGame"
            v-if="isSpymaster"
          >
            New Game
          </v-btn>
          <v-btn
            color="red darken-2"
            @click="newGame"
            :to="{ name: 'Home' }"
          >
            Leave Room
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>

</template>

<script>
import Scoreboard from "@/components/Scoreboard";
import { mapState, mapGetters, mapMutations } from "vuex";

export default {
  components: { Scoreboard },
  data() {
    return {
      fab: false
    };
  },
  computed: {
    ...mapState(["room", "game", "connected"]),
    ...mapGetters(["gameWon", "isSpymaster"]),
    isFirstTurn() {
      if (!this.connected) {
        return true;
      }
      if (this.game.board) {
        return Object.values(this.game.board).every(e => e === false);
      }
      return true;
    }
  },
  methods: {
    ...mapMutations(["reset_room"]),
    newGame(reset) {
      // reset spymaster state and go to player view
      // emit message to start a new game
      const params = {
        room: this.room
      };
      if (reset === true) {
        this.reset_room();
        params["newGame"] = true;
      }
      this.$socket.emit("regenerate", params);
    },
    closeRoom() {
      this.$socket.emit("close_room", { room: this.room });
    }
  }
};
</script>

<style lang="scss" scoped>
.v-speed-dial {
  top: 75px;
}
#show-more {
  bottom: 75px;
}
</style>
