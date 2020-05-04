<template>
  <v-bottom-navigation
    app
    grow
    max-height="48px"
  >
    <v-btn @click.stop="drawer = !drawer">
      <span>Menu</span>
      <v-icon medium>mdi-menu</v-icon>
    </v-btn>
    <v-btn
      replace
      :to="{ name: 'Player', params: { room: room }}"
      v-if="room && connected && !error"
    >
      <span>Agent</span>
      <v-badge
        color="secondary"
        :content="players"
      >
        <v-icon medium>mdi-account</v-icon>
      </v-badge>
    </v-btn>

    <v-btn
      replace
      :to="{ name: 'Spymaster', params: { room: room }}"
      v-if="room && connected && !error"
    >
      <span>Spymaster</span>
      <v-badge
        :color="spymastersColor"
        :content="spymasters"
      >
        <v-icon medium>mdi-library</v-icon>
      </v-badge>
    </v-btn>
    <v-btn
      v-if="game && game.players"
      @click.stop="infoDrawer = !infoDrawer"
    >
      <span>Game Info</span>
      <v-icon medium>mdi-information</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState(["connected", "room", "error", "game"]),
    drawer: {
      get() {
        return this.$store.state.drawer;
      },
      set(v) {
        return this.$store.commit("set_drawer", v);
      }
    },
    infoDrawer: {
      get() {
        return this.$store.state.info_drawer;
      },
      set(v) {
        return this.$store.commit("set_info_drawer", v);
      }
    },
    players() {
      if (this.game.players)
        return (
          Object.keys(this.game.players.players).length -
          this.game.players.spymasters.length
        ).toString();
      return "0";
    },
    spymasters() {
      if (this.game.players)
        return this.game.players.spymasters.length.toString();
      return "0";
    },
    spymastersColor() {
      if (this.game.players) {
        if (
          this.game.players &&
          this.game.players.spymasters.length > this.game.options.teams
        )
          return "error";
        else if (this.game.players.spymasters.length === 0) return "secondary";
        return "primary";
      }
      return "";
    }
  }
};
</script>

<style>
</style>
