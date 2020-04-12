<template>
  <v-app-bar
    app
    fixed
    :color="getColor"
    v-if="!error && room"
    class="telegram"
  >
    <v-toolbar-title class="cn-text headline">{{room}}</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-title
      v-if="isFirstTurn"
      class="cn-text"
    >{{getTurn}}</v-toolbar-title>
    <v-toolbar-title
      v-else
      class="cn-text headline"
      id="scoreboard"
    >
      <span class="red--text text--darken-1">{{tileCounts.flipped.R}}</span>
      <span
        style="padding: 0 10px;"
        v-if="!'G' in tileCounts.flipped"
      >
        <v-avatar size="32">
          <img
            src="@/assets/logo-64x64.png"
            alt="codenames logo"
          />
        </v-avatar>
      </span>
      <span v-else> - </span>
      <span class="blue--text text--darken-1">{{tileCounts.flipped.B}}</span>
      <template v-if="'G' in tileCounts.flipped">
        <span> - </span>
        <span class="green--text text--lighten-1">{{tileCounts.flipped.G}}</span>
      </template>
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
import { mapState, mapGetters } from "vuex";

export default {
  computed: {
    ...mapState(["connected", "room", "error", "game", "turn"]),
    ...mapGetters(['tileCounts']),
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
