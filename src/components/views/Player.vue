<template>
  <v-container grid-list-sm pa-0>
    <v-layout row wrap>
      <v-flex xs12 sm3 md3 v-for="(team, word) in game.board">
        <v-card :color="getColor(team)" tile flat dark>
          <v-card-text px-0>
            {{word}}
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    
  </v-container>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'player',
  computed: {
    ...mapState(['connected', 'room', 'username', 'game']),
  },
  mounted() {
    if (!this.username) this.set_username('#unknown');
    if (!this.room) this.set_room(this.$route.params.room);
    const params = {
      username: this.username,
      room: this.room,
    };
    this.$socket.emit('join', params);
  },
  methods: {
    ...mapMutations(['set_room', 'set_username']),
    getColor(id) {
      switch (id) {
        case 'R':
          return 'red darken-1';
        case 'G':
          return 'green lighten-1';
        case 'B':
          return 'blue darken-1';
        case 'O':
          return 'black--text amber lighten-2';
        case 'X':
          return 'grey darken-4';
        case '-':
          return 'black--text black';
        default:
          return '';
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
