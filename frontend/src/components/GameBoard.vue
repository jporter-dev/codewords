<template>
  <v-container fluid grid-list-md fill-height pa-0 v-if="role">
    <v-layout column>
      <slot></slot>
      <game-controls></game-controls>
      <v-flex pa-0 v-for="row in gridRows" :key="row">
        <v-layout row wrap :fill-height="$vuetify.breakpoint.mdAndUp">
          <v-flex d-flex class="cn-card" v-for="cell in gridCells" @click="showFlipCard(getWord(row, cell))" :key="cell">
            <v-fade-transition appear>
              <v-card tile :color="getColor(getWord(row, cell), getTeam(getWord(row, cell)))" class="text-xs-center">
                <v-layout fill-height align-center ma-0>
                  <v-flex pa-0>
                    <v-card-text class="cn-text cn-text--upcase" :class="{'font-weight-bold': $vuetify.breakpoint.mdAndUp}" v-resize-text="{ratio: 1.1}">
                      {{getWord(row, cell)}}
                    </v-card-text>
                  </v-flex>
                </v-layout>
              </v-card>
            </v-fade-transition>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
    <v-dialog v-model="confirmShow" max-width="290">
      <v-card :color="getColor(confirmCard, getTeam(confirmCard))" class="text-xs-center">
        <v-card-text class="headline cn-text cn-text--upcase">
          {{confirmCard}}
        </v-card-text>
        <v-card-actions>
          <v-btn block large color="secondary" @click.stop="flipCard">Confirm</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-snackbar
      color="red darken-3"
      :vertical="true"
      v-model="agentAlert"
    >
      Only the Spymaster can flip cards.
      <v-btn flat :to="{ name: 'Spymaster', params: { room: room }}">Switch to Spymaster</v-btn>
    </v-snackbar>
  </v-container>
</template>

<script>
  import { mapState, mapGetters, mapMutations } from 'vuex';
  import GameControls from '@/components/GameControls'

  export default {
    name: 'game-board',
    components: { GameControls },
    props: ['role'],
    data() {
      return {
        confirmShow: false,
        confirmCard: null,
        spymaster: 'Spymaster',
        agentAlert: false,
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
    watch: {
      '$store.state.error': {
        immediate: true,
        handler () {
          // if (this.$store.state.error !== null)
            // this.$router.push({path: '/home'})
        }
      }
    },
    computed: {
      ...mapState(['connected', 'room', 'username', 'game']),
      ...mapGetters(['words', 'gameWon']),
      cards() {
        if (this.isSpymaster()) {
          return this.game.solution;
        }
        return this.game.board;
      },
      gridRows() {
        if (this.words) {
          switch (this.$vuetify.breakpoint.name) {
            case 'xs': return '1'
            case 'sm': return '1'
            default: return Math.sqrt(this.words.length)
          }
        }
        return 0;
      },
      gridCells() {
        if (this.words) {
          return this.words.length / this.gridRows
        }
        return 0;
      },
      responsiveClass() {
        switch (this.$vuetify.breakpoint.name) {
          case 'xs': return 'body-2';
          case 'lg': return 'display-1';
          case 'xl': return 'display-1';
          default: return 'headline';
        }
      },
    },
    methods: {
      ...mapMutations(['set_room', 'set_username']),
      isSpymaster() {
        return this.role === this.spymaster;
      },
      getWord(row, cell) {
        const temp = (((row - 1) * this.gridRows) + (cell - 1));
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
              return 'red darken-3';
            case 'G':
              return 'green lighten-1';
            case 'B':
              return 'blue darken-2';
            case 'O':
              return 'black--text grey lighten-3';
            case 'X':
              return 'grey darken-4';
            case '-':
              return 'black--text grey lighten-3';
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
              return 'grey--text text--lighten-1';
            default:
              return '';
          }
        }
        return 'grey darken-2';
      },
      showFlipCard(word) {
        if (this.isSpymaster() && !this.game.board[word]) {
          this.confirmCard = word;
          this.confirmShow = true;
        }
        // if not spymaster, display warning
        if (!this.isSpymaster()) {
          this.agentAlert = true;
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
<style lang="scss" scoped>
.cn-card {
  cursor: pointer;
  flex-basis: 0;
  flex-shrink: 0;
  flex-grow: 1;
}

.cn-text {
  letter-spacing: 2px!important;
}
</style>
