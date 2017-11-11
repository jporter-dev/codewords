<template>
  <v-container grid-list-sm pa-0>
    <v-layout row wrap v-for="i in gridSize">
      <v-flex class="cn-card" v-for="x in gridSize">
        <v-card :color="getColor(game.solution[game.words[x*i-1]])" tile flat dark>
          <v-card-text px-0>
            {{game.words[x*i-1]}}
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
    gridSize() {
      let grid = 0;
      if (this.game.words) {
        grid = Math.sqrt(this.game.words.length);
      }
      return grid;
    },
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
.cn-card {
  flex-basis: 0;
  flex-grow: 1;
}
</style>
