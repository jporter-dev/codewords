<template>
  <v-dialog
    v-model="showDialog"
    max-width="350"
  >
    <v-card
      color="secondary"
      class="telegram"
    >
      <v-card-title
        class="justify-center telegram"
        :class="winner"
      >
        Game Over!
      </v-card-title>
      <v-card-title class="justify-center">
        Cards remaining:<scoreboard class="ml-2"></scoreboard>
      </v-card-title>
      <v-card-text class="text-center">
        Start a new game with current game settings or create a new lobby.
      </v-card-text>
      <v-card-actions class="justify-center">
        <v-btn
          color="primary"
          @click="new_game(true)"
        >
          New Game
        </v-btn>
        <v-btn
          color="red darken-2"
          :to="{ name: 'Home' }"
        >
          Leave Game
        </v-btn>
      </v-card-actions>
      <v-divider></v-divider>
      <v-card-title class="justify-center">
        <h5>Enjoying Codenames.tv?</h5>
      </v-card-title>
      <v-card-actions>
        <coffee-button></coffee-button>
      </v-card-actions>
      <v-card-actions class="justify-center">
        <a
          :href="$store.state.feedback_form"
          target="_BLANK"
        >
          Or leave some feedback...
        </a>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import Scoreboard from "@/components/Scoreboard";
import CoffeeButton from "@/components/misc/CoffeeButton";
import { mapGetters, mapState, mapMutations } from "vuex";

export default {
  components: { CoffeeButton, Scoreboard },
  data() {
    return {
      showDialog: false
    };
  },
  computed: {
    ...mapGetters(["gameWon", "tileCounts"]),
    winner() {
      let teamMap = {
        R: "red",
        B: "blue",
        G: "green",
        X: "black"
      };
      let winner = "secondary";
      Object.keys(this.tileCounts.flipped).map(team => {
        if (this.tileCounts.flipped[team] === this.tileCounts.total[team]) {
          winner = teamMap[team];
        }
      });
      return winner;
    }
  },
  methods: {
    ...mapMutations(["new_game"])
  },
  watch: {
    gameWon: {
      immediate: true,
      handler(won) {
        if (won) {
          this.showDialog = true;
        }
      }
    }
  }
};
</script>

<style>
</style>
