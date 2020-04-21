<template>
  <v-app id="codenames">
    <app-drawer></app-drawer>
    <app-toolbar></app-toolbar>
    <game-controls></game-controls>
    <v-content>
      <v-container
        fluid
        fill-height
        pa-0
        class="align-start"
      >
        <router-view></router-view>
      </v-container>
    </v-content>
    <app-nav></app-nav>
    <v-dialog
      :value="disconnected"
      persistent
      max-width="300px"
      overlay-opacity=".75"
      overlay-color="black"
    >
      <v-card>
        <v-card-title>{{ $t('unable to connect') }}</v-card-title>
        <v-card-text>
          {{ $t('please stand by') }}
          <v-progress-linear indeterminate color="white" class="mb-0"></v-progress-linear>
        </v-card-text>
        <v-card-actions>
          <v-btn block color="secondary">{{ $t('report an issue') }}</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>
import AppToolbar from "@/components/app/Toolbar";
import AppDrawer from "@/components/app/Drawer";
import AppNav from "@/components/app/Nav";
import GameControls from "@/components/game/Controls";

import { mapState } from "vuex";

export default {
  name: "app",
  components: { AppDrawer, AppNav, AppToolbar, GameControls },
  data() {
    return {
      drawer: undefined,
      disconnected: false,
      disconnect_delay: null
    };
  },
  computed: {
    ...mapState(["connected"])
  },
  watch: {
    connected: {
      immediate: true,
      handler(val) {
        if (this.disconnect_delay) clearTimeout(this.disconnect_delay);
        if (val) {
          // generate a username
          this.disconnected = false;
          this.$store.commit("set_current_sid", this.$socket.id);
          if (!this.$store.state.starting_sid)
            this.$store.commit("set_starting_sid", this.$socket.id);
        } else {
          // reset delay timer
          this.disconnect_delay = setTimeout(() => {
            return (this.disconnected = true);
          }, 3000);
        }
      }
    }
  },
  created() {
    this.$vuetify.theme.dark = true;
  }
};
</script>

<style lang="scss">
html,
body {
  background: #303030;
}
.cn-text {
  font-family: "Special Elite", "Courier New", Courier, "Lucida Sans Typewriter",
    "Lucida Typewriter", monospace !important;
  letter-spacing: 1px !important;
  &--upcase {
    text-transform: uppercase;
  }
  &--caps {
    text-transform: capitalize;
  }
}
#scoreboard {
  font-weight: bold;
}

.telegram {
  position: relative;
}

.telegram::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: url("https://images.unsplash.com/photo-1532153259564-a5f24f261f51?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2550&h=500&q=80");
  opacity: 0.4;
}

.telegram > div {
  position: relative;
}
</style>
