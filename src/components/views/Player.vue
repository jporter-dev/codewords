<template>
  <v-container grid-list-sm pa-0>
    <v-layout row wrap v-for="row in gridSize">
      <v-flex class="cn-card" v-for="cell in gridSize" @click="flipCard(getWord(row, cell))">
        <v-card :color="getColor(getWord(row, cell), game.board[getWord(row, cell)])" tile flat dark>
          <v-card-text px-0>
            {{getWord(row, cell)}}
          </v-card-text>
          <v-card-text px-0 v-if="getWord(row, cell) === 'confirm'">
            Confirm
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
  data() {
    return {
      confirmCard: null,
    };
  },
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
    getWord(row, cell) {
      const temp = (((row - 1) * this.gridSize) + (cell - 1));
      return this.game.words[temp];
    },
    getColor(word, id) {
      if (this.confirmCard === word) {
        return 'grey darken-4';
      }
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
    flipCard(word) {
      if (!this.game.board[word]) {
        // check if clicked card has already been clicked
        if (this.confirmCard === word) {
          // reset confirmCard
          this.confirmCard = null;
          // send request to confirm the card
          const params = {
            card: word,
            room: this.room,
          };
          this.$socket.emit('flip_card', params);
        } else {
          // otherwise set confirm to current word to require a second click
          this.confirmCard = word;
        }
      } else {
        console.log('card aleady flipped');
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cn-card {
  cursor: pointer;
  flex-basis: 0;
  flex-grow: 1;
}
</style>
