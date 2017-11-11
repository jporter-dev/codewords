<template>
  <v-app dark>
    <main>
      <v-content>
        <v-container fluid pb-5 mb-4>
          <router-view>
          </router-view>
        </v-container>
      </v-content>
    </main>
    <v-bottom-nav :value="true" class="secondary">
      <v-btn flat :to="{ name: 'Home' }">
        <v-icon medium>home</v-icon> Home
      </v-btn>
      <v-btn flat :to="{ name: 'Player', params: { room: room }}">
        <v-icon medium>person</v-icon> Player
      </v-btn>
      <v-btn flat :to="{ name: 'Spymaster', params: { room: room }}">
        <v-icon medium>local_library</v-icon> Spymaster
      </v-btn>
      <v-btn flat v-if="room" class="white--text">
        <span class="body-2">{{ room }}</span>
        <span>Room ID</span>
      </v-btn>
    </v-bottom-nav>
  </v-app>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'app',
  computed: {
    ...mapState(['room']),
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
