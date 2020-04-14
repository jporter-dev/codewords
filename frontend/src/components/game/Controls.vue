<template>
  <div>
    <v-dialog
      v-model="gameWon"
      max-width="290"
      persistent
    >
      <v-card
        color="secondary"
        class="telegram"
      >
        <v-card-title class="justify-center">Game Over!</v-card-title>
        <v-card-title class="justify-center">
          <scoreboard></scoreboard>
        </v-card-title>
        <v-card-text>Start a new game with current game settings or create a new lobby.</v-card-text>
        <v-card-actions class="justify-center">
          <v-btn
            color="primary"
            @click="newGame"
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

    <v-speed-dial
      v-model="fab"
      top
      right
      fixed
      open-on-hover
      direction="bottom"
      transition="slide-y-reverse-transition"
      v-if="room && spymasterReveal && (isFirstTurn || gameWon)"
    >
      <template v-slot:activator>
        <v-btn
          v-model="fab"
          color="secondary"
          small
          dark
          fab
        >
          <v-icon v-if="fab">mdi-close</v-icon>
          <v-icon v-else>mdi-settings</v-icon>
        </v-btn>
      </template>
      <v-tooltip
        left
        v-if="gameWon"
      >
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
      <v-tooltip
        left
        v-else
      >
        <template v-slot:activator="{ on }">
          <v-btn
            fab
            dark
            small
            color="green darken-2"
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
            :to="{ name: 'Home' }"
          >
            <v-icon>mdi-door-closed</v-icon>
          </v-btn>
        </template>
        <span>Leave Room</span>
      </v-tooltip>
    </v-speed-dial>
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
    ...mapState(["room", "game", "connected", "spymasterReveal"]),
    ...mapGetters(["gameWon"]),
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
  watch: {
    gameWon(val) {
      if (val) this.fab = true;
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
        this.$router.push({ path: `/${this.room}/player` });
      }
      this.$socket.emit("regenerate", params);
    }
  }
};
</script>

<style lang="scss" scoped>
.v-speed-dial {
  top: 75px;
}
</style>
