<template>
  <v-app dark>
    <main>
      <v-content>
        <v-toolbar :color="getColor" dark fixed v-if="room">
          <v-toolbar-title>{{room}}</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-title>{{getTurn}}</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn flat large @click="nextTurn">
            <v-icon medium>skip_next</v-icon>
          </v-btn>
        </v-toolbar>

        <v-container fill-height fluid pr-2 pl-2>
          <router-view>
          </router-view>
        </v-container>

        <v-bottom-nav :value="this.room" class="secondary">
          <v-btn flat replace :to="{ name: 'Home' }">
            <v-icon medium>home</v-icon> Home
          </v-btn>
          <v-btn flat replace :to="{ name: 'Player', params: { room: room }}">
            <v-icon medium>person</v-icon> Agent
          </v-btn>
          <v-btn flat replace :to="{ name: 'Spymaster', params: { room: room }}">
            <v-icon medium>local_library</v-icon> Spymaster
          </v-btn>
        </v-bottom-nav>

      </v-content>
    </main>
  </v-app>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'app',
  data() {
    return {
      showSidebar: false,
      showError: false,
    };
  },
  computed: {
    ...mapState(['room', 'error', 'game', 'turn']),
    getColor() {
      switch (this.turn) {
        case 'R':
          return 'red darken-1';
        case 'G':
          return 'green lighten-1';
        case 'B':
          return 'blue darken-1';
        default:
          return 'secondary';
      }
    },
    getTurn() {
      switch (this.turn) {
        case 'R':
          return 'Red\'s Turn';
        case 'G':
          return 'Green\'s Turn';
        case 'B':
          return 'Blue\'s Turn';
        default:
          return '';
      }
    },
  },
  methods: {
    ...mapMutations(['set_turn']),
    nextTurn() {
      if (this.turn === 'R') {
        this.set_turn('B');
      } else if (this.turn === 'B') {
        if (this.game.teams === 3) {
          this.set_turn('G');
        } else {
          this.set_turn('R');
        }
      } else {
        this.set_turn('R');
      }
    },
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*margin-top: 60px;*/
}

/* transitions */

.fade-enter-active {
  transition: all 1s ease;
}
.fade-leave-active {
  transition: all .2s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
