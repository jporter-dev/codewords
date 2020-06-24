<template>
  <v-navigation-drawer
    temporary
    right
    app
    v-model="infoDrawer"
    width="275"
  >
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="title">
          Room ID: {{room}}
        </v-list-item-title>
        <v-list-item-subtitle v-if="game.options">
          Dictionary: {{game.options.custom ? "Custom" : game.options.dictionary}}
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item @click="newGame(false)">
      <v-list-item-icon>
        <v-icon>mdi-shuffle</v-icon>
      </v-list-item-icon>
      <v-list-item-content>
        <v-list-item-title>Generate New Words</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-divider></v-divider>
    <template v-if="game.players">
      <v-list-item>
        <v-list-item-subtitle>Current Players</v-list-item-subtitle>
        <v-list-item-avatar>
          <v-chip small>{{Object.keys(game.players.players).length}}</v-chip>
        </v-list-item-avatar>
      </v-list-item>
      <v-list-item
        v-for="id in game.players.spymasters"
        :key="id"
        :title="id"
      >
        <v-list-item-icon>
          <v-icon>mdi-library</v-icon>
        </v-list-item-icon>
        <v-list-item-title>{{game.players.players[id]}}</v-list-item-title>
      </v-list-item>
      <template v-for="(name,id) in game.players.players">
        <v-list-item
          v-if="game.players.spymasters.indexOf(id) < 0"
          :key="id"
          :title="id"
        >
          <v-list-item-icon>
            <v-icon>mdi-account</v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{name}}</v-list-item-title>
        </v-list-item>
      </template>
    </template>
  </v-navigation-drawer>
</template>

<script>
import { mapState, mapGetters, mapMutations } from "vuex";

export default {
  computed: {
    ...mapState(["connected", "game", "room"]),
    ...mapGetters(["username", "isSpymaster"]),
    infoDrawer: {
      get() {
        return this.$store.state.info_drawer || false;
      },
      set(v) {
        return this.$store.commit("set_info_drawer", v);
      }
    }
  },
  methods: {
    ...mapMutations(["new_game"]),
    newGame(reset) {
      this.infoDrawer = false;
      this.new_game(reset);
    }
  },
  beforeCreate() {
    this.infoDrawer = false;
  }
};
</script>

<style>
</style>
