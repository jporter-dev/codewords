<template>
  <v-app-bar
    app
    fixed
    dense
    :color="getColor"
    v-if="!error && room && game.board"
    class="telegram"
  >
    <v-toolbar-title v-if="isFirstTurn">
      <invite-link></invite-link>
    </v-toolbar-title>
    <v-toolbar-title
      class="cn-text headline"
      id="scoreboard"
      v-else
    >
      <scoreboard></scoreboard>
    </v-toolbar-title>
    <v-toolbar-title
      class="cn-text ml-4 mt-1 grow text-center"
      v-if="isFirstTurn"
    >
      {{getTurn}}
    </v-toolbar-title>
    <v-spacer v-else></v-spacer>
    <timer></timer>
  </v-app-bar>
</template>

<script>
import Scoreboard from "@/components/Scoreboard";
import InviteLink from "@/components/misc/InviteLink";
import Timer from "@/components/game/Timer";

import { mapState, mapGetters } from "vuex";

export default {
  components: { Scoreboard, InviteLink, Timer },
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

      const team_starts = `${this.$t('team')} ${this.$t('starts')}`
      switch (this.turn) {
        case "R":
          return `${this.$t('red')} ${team_starts}`;
        case "G":
          return `${this.$t('green')} ${team_starts}`;
        case "B":
          return `${this.$t('blue')} ${team_starts}`;
        default:
          return "";
      }
    }
  }
};
</script>

<style>
</style>

<i18n src="@/plugins/translations/game.json"/>
