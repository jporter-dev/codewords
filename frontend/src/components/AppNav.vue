<template>
  <v-bottom-navigation app class="telegram">
    <v-btn
      replace
      :to="{ name: 'Home' }"
    >
      <span>Home</span>
      <v-icon medium>mdi-home</v-icon>
    </v-btn>
    <v-btn
      color="red darken-3"
      v-if="!connected"
      value="false"
    >
      <span>Not Connected</span>
      <v-icon medium>mdi-alert</v-icon>
    </v-btn>
    <v-btn
      replace
      :to="{ name: 'Player', params: { room: room }}"
      v-if="room && connected && !error"
    >
      <span>Agent</span>
      <v-icon medium>mdi-account</v-icon>
    </v-btn>
    <v-btn
      replace
      :to="{ name: 'Spymaster', params: { room: room }}"
      v-if="room && connected && !error"
    >
      <span>Spymaster</span>
      <v-icon medium>mdi-library</v-icon>
    </v-btn>
    <v-btn
      @click.stop="drawer = !drawer"
      to="#"
    >
      <span>Menu</span>
      <v-icon medium>mdi-menu</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState(['connected', 'room', 'error'])
  }
};
</script>

<style>
</style>
