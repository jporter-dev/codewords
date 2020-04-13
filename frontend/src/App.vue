<template>
  <v-app id="codenames">
    <app-toolbar></app-toolbar>
    <v-content>
      <v-container fluid fill-height pa-0 class="align-start">
        <router-view></router-view>
      </v-container>
    </v-content>
    <app-nav></app-nav>
  </v-app>
</template>

<script>
import AppToolbar from "@/components/AppToolbar";
import AppNav from "@/components/AppNav";
import CoffeeButton from "@/components/CoffeeButton";

export default {
  name: "app",
  components: { AppToolbar, AppNav, CoffeeButton },
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
  font-family: "Special Elite", "Courier New", Courier, "Lucida Sans Typewriter", "Lucida Typewriter", monospace!important;
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
  background: url('/img/paper-texture.png');
  opacity: 0.4;
}

.telegram > div {
  position: relative;
}
</style>
