<template>
  <v-app id="codenames">
    <app-drawer></app-drawer>
    <info-drawer></info-drawer>
    <app-toolbar></app-toolbar>
    <app-notification></app-notification>
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
    <connection-dialog></connection-dialog>
  </v-app>
</template>

<script>
import AppToolbar from "@/components/app/Toolbar";
import AppDrawer from "@/components/app/Drawer";
import AppNotification from "@/components/app/Notification";
import AppNav from "@/components/app/Nav";
import InfoDrawer from "@/components/app/InfoDrawer";
import ConnectionDialog from "@/components/misc/ConnectionDialog";

import { mapState } from "vuex";

export default {
  name: "app",
  components: {
    AppDrawer,
    InfoDrawer,
    AppNav,
    AppNotification,
    AppToolbar,
    ConnectionDialog
  },
  data() {
    return {
      drawer: undefined
    };
  },
  computed: {
    ...mapState(["connected", "idleVue"])
  },
  watch: {
    "idleVue.isIdle": {
      handler(val) {
        if (val) this.$socket.disconnect();
        else this.$socket.connect();
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
