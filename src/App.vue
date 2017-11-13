<template>
  <v-app dark>
    <main>
      <v-content>
        <v-toolbar :color="getColor" dark fixed scroll-off-screen v-if="room">
          <v-toolbar-title>{{room}}</v-toolbar-title>
          <v-spacer></v-spacer>
          <!-- <v-toolbar-title class="hidden-xs-only">{{getTurn}}</v-toolbar-title> -->
          <!-- <v-spacer></v-spacer> -->
          <v-btn flat large @click="nextTurn">
            Next Turn<v-icon medium>skip_next</v-icon>
          </v-btn>
        </v-toolbar>

        <v-container fill-height fluid pr-2 pl-2 style="overflow-y: auto;">
          <router-view>
          </router-view>
        </v-container>

        <v-navigation-drawer
          v-model="drawer"
          temporary
          dark
          right
        >
          <v-list class="pa-1">
            <v-list-tile avatar tag="div">
              <v-list-tile-action>
                <v-btn icon @click.stop="drawer = !drawer">
                  <v-icon>chevron_right</v-icon>
                </v-btn>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>Codenames</v-list-tile-title>
              </v-list-tile-content>
              <v-list-tile-avatar>
                <img src="/static/images/secret-agent-256.png" />
              </v-list-tile-avatar>
            </v-list-tile>
          </v-list>
          <v-list class="pt-0" dense>
            <v-divider light></v-divider>
            <v-list-tile v-for="item in helpMenu" :key="item.title" router :to="item.path" :href="item.href">
              <v-list-tile-action>
                <v-icon>{{item.icon}}</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>{{item.title}}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-navigation-drawer>

        <v-bottom-nav value="true" class="secondary">
          <v-btn flat replace :to="{ name: 'Home' }">
            <v-icon medium>home</v-icon> Home
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn flat replace :to="{ name: 'Player', params: { room: room }}" v-if="room">
            <v-icon medium>person</v-icon> Agent
          </v-btn>
          <v-btn flat replace :to="{ name: 'Spymaster', params: { room: room }}" v-if="room">
            <v-icon medium>local_library</v-icon> Spymaster
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn flat @click.stop="drawer = !drawer">
            <v-icon medium>help_outline</v-icon> Help
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
      drawer: false,
      showSidebar: false,
      showError: false,
      helpMenu: [
        {
          title: 'How to Play',
          icon: 'import_contacts',
          path: '/help',
        },
        {
          title: 'Contact',
          icon: 'email',
          href: 'mailto:joshporter1@gmail.com?subject=Codenames Support',
        },
        {
          title: 'Contribute',
          icon: 'code',
          href: 'https://github.com/joshporter1/codenames',
        },
        {
          title: 'Donate',
          icon: 'attach_money',
          href: 'https://paypal.me/joshporter1',
        },
      ],
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
html, body { background-color: #303030; }

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
