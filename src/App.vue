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
            <v-icon medium>person</v-icon> Player
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
import { mapState } from 'vuex';

export default {
  name: 'app',
  data() {
    return {
      showSidebar: false,
      showError: false,
      currentTeam: '',
    };
  },
  computed: {
    ...mapState(['room', 'error', 'game']),
    getColor() {
      switch (this.currentTeam) {
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
    getCurrentTeam() {
      if (!this.currentTeam) {
        this.currentTeam = this.game.starting_color;
      }
      return this.currentTeam;
    },
    getTurn() {
      switch (this.getCurrentTeam) {
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
    nextTurn() {
      if (this.currentTeam === 'R') {
        this.currentTeam = 'B';
      } else if (this.currentTeam === 'B') {
        if (this.game.teams === 3) {
          this.currentTeam = 'G';
        } else {
          this.currentTeam = 'R';
        }
      } else {
        this.currentTeam = 'R';
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
