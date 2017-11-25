<template>
  <v-container fluid grid-list-sm mt-5 mb-5 pa-0 v-if="role">
    <v-layout row wrap v-for="row in gridSize" :key="row">
      <v-flex class="cn-card" v-for="cell in gridSize" @click="showFlipCard(getWord(row, cell))" :key="cell">
        <v-fade-transition appear>
          <v-card :color="getColor(getWord(row, cell), getTeam(getWord(row, cell)))" tile flat dark>
            <v-card-text px-0 class="body-2 hidden-sm-and-up">
              {{getWord(row, cell)}}
            </v-card-text>
            <v-card-text px-0 class="display-1 hidden-xs-only">
              {{getWord(row, cell)}}
            </v-card-text>
          </v-card>
        </v-fade-transition>
      </v-flex>
    </v-layout>
    <v-dialog v-model="confirmShow">
      <v-card :color="getColor(confirmCard, getTeam(confirmCard))" tile flat dark>
        <v-card-text class="headline">
          {{confirmCard}}
        </v-card-text>
        <v-card-actions>
          <v-btn block large color="secondary" @click.stop="flipCard">Confirm</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
  import { mapState, mapGetters, mapMutations } from 'vuex';

  export default {
    name: 'game-board',
    props: ['role'],
    data() {
      return {
        confirmShow: false,
        confirmCard: null,
        spymaster: 'Spymaster',
      };
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
    computed: {
      ...mapState(['connected', 'room', 'username', 'game']),
      ...mapGetters(['words']),
      cards() {
        if (this.isSpymaster()) {
          return this.game.solution;
        }
        return this.game.board;
      },
      gridSize() {
        let grid = 0;
        if (this.words) {
          grid = Math.sqrt(this.words.length);
        }
        return grid;
      },
    },
    methods: {
      ...mapMutations(['set_room', 'set_username']),
      isSpymaster() {
        return this.role === this.spymaster;
      },
      getWord(row, cell) {
        const temp = (((row - 1) * this.gridSize) + (cell - 1));
        return this.words[temp];
      },
      getTeam(word) {
        if (word) {
          return this.cards[word];
        }
        return null;
      },
      getColor(word, id) {
        // already flipped cards
        // if word is null - for starting team card
        // if spymaster and word isn't flipped
        // if not spymaster and word is flipped
        if (!word || (!this.isSpymaster() && this.game.board[word]) ||
          (this.isSpymaster() && !this.game.board[word])) {
          switch (id) {
            case 'R':
              return 'red darken-1';
            case 'G':
              return 'green lighten-1';
            case 'B':
              return 'blue darken-1';
            case 'O':
              return 'black--text grey lighten-3';
            case 'X':
              return 'grey darken-4';
            case '-':
              return 'black--text black';
            default:
              return '';
          }
        } else if (this.isSpymaster() && this.game.board[word]) {
          switch (id) {
            case 'R':
              return 'red--text text--darken-1';
            case 'G':
              return 'green--text text--lighten-1';
            case 'B':
              return 'blue--text text--darken-1';
            case 'O':
              return 'grey--text text--lighten-1';
            case 'X':
              return 'grey darken-4';
            case '-':
              return 'black--text black';
            default:
              return '';
          }
        }
        return '';
      },
      showFlipCard(word) {
        if (this.isSpymaster() && !this.game.board[word] && this.cards[word] !== '-') {
          this.confirmCard = word;
          this.confirmShow = true;
        }
      },
      flipCard() {
        // check if card not already clicked and role is spymaster
        // and not a blackout square
        if (this.isSpymaster() && !this.game.board[this.confirmCard] && this.confirmCard) {
          // send request to confirm the card
          const params = {
            card: this.confirmCard,
            room: this.room,
          };
          this.$socket.emit('flip_card', params);
          // reset confirmCard
          this.confirmCard = null;
          this.confirmShow = false;
        } else {
          // card already flipped
          this.confirmCard = null;
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
  flex-shrink: 0;
  flex-grow: 1;
  white-space: nowrap;
}
</style>