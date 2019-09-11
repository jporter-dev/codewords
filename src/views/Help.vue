<template>
  <v-layout align-start justify-center row fill-height>
    <v-flex md6>
      <v-card tile flat>
        <v-card-text px-0 class='text-xs-left'>
          <h4>Getting Started</h4>
          <p>
            This application is designed to be played on multiple devices. The "agent"
            view can be loaded on a TV or mobile devies, and the "spymaster" view
            should be activated on the phones of the spymasters.
          </p>
          <h4 class="header">How to Play</h4>
          <p>Codenames consists of two teams with two roles on each team: a spymaster and field agents.</p>
          <p>
            <a href="https://www.youtube.com/watch?v=zQVHkl8oQEU">Watch an instructional video.</a>
          </p>
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: 'help',
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
