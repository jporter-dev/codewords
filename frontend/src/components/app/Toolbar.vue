<template>
  <v-app-bar
    app
    fixed
    :color="getColor"
    v-if="!error && room"
    class="telegram"
  >
    <v-toolbar-title v-if="isFirstTurn">
      <invite-link></invite-link>
    </v-toolbar-title>
    <v-toolbar-title
      v-else
      class="cn-text headline"
      id="scoreboard"
    >
      <scoreboard></scoreboard>
    </v-toolbar-title>
    <v-spacer></v-spacer>

    <v-toolbar-title
      class="cn-text"
      v-if="isFirstTurn"
    >
      {{getTurn}}
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
import Scoreboard from "@/components/Scoreboard";
import InviteLink from "@/components/misc/InviteLink";
import { mapState, mapGetters } from "vuex";

export default {
  components: { Scoreboard, InviteLink },
  computed: {
    ...mapState(["connected", "room", "error", "game", "turn"]),
    ...mapGetters(["tileCounts"]),
    isFirstTurn() {
      if (!this.connected) {
        return true;
      }
      if (this.game.board) {
        return Object.values(this.game.board).every(e => e === false);
      }
      return true;
    },
    getColor() {
      // override bar color if ws not connected
      if (!this.connected) {
        return "red darken-3";
      }
      if (this.isFirstTurn) {
        switch (this.turn) {
          case "R":
            return "red darken-3";
          case "G":
            return "green lighten-1";
          case "B":
            return "blue darken-2";
          default:
            return "secondary";
        }
      }
      return "secondary";
    },
    getTurn() {
      // override starting team text if ws is not connected
      if (!this.connected) {
        return "Unable to connect to server.";
      }
      switch (this.turn) {
        case "R":
          return "Red Team Starts";
        case "G":
          return "Green Team Starts";
        case "B":
          return "Blue Team Starts";
        default:
          return "";
      }
    }
  }
};
</script>

<style>
</style>
