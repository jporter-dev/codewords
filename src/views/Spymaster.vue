<template>
  <div style="width: 100%;">
    <v-layout align-center justify-center text-xs-center row wrap mb-5 v-if="!spymasterReveal">
      <v-flex sm8 xs12>
        <v-alert outline type="warning" :value="true">
          <b>Warning!</b> There should only be two spymasters per game.
        </v-alert>
        <v-btn block large color="success" @click="reveal_spymaster" id="spymaster-btn">I understand. Make me a spymaster!</v-btn>
      </v-flex>
    </v-layout>
    <template v-if="spymasterReveal">
      <v-btn block large v-if="gameWon" color="success" @click.native="newGame">New Game</v-btn>
      <v-btn block large v-if="isFirstTurn && !gameWon" color="primary" @click.native="newGame" id="shuffle-btn">Shuffle New Words</v-btn>
      <game-board :role="role" v-if="spymasterReveal"></game-board>
    </template>
  </div>
</template>

<script>
import GameBoard from '@/components/GameBoard';
import { mapState, mapMutations, mapGetters } from 'vuex';

export default {
  name: 'spymaster',
  components: {
    GameBoard,
  },
  computed: {
    ...mapGetters(['gameWon']),
    ...mapState(['room', 'username', 'spymasterReveal']),
    role() {
      if (!this.spymasterReveal) {
        return null;
      }
      return this.$route.name;
    },
    isFirstTurn() {
      if (!this.connected) {
        return true;
      }
      if (this.game.board) {
        return Object.values(this.game.board).every(e => e === false);
      }
      return true;
    },
  },
  methods: {
    ...mapMutations(['set_room', 'set_username', 'reveal_spymaster']),
    newGame() {
      // emit message to start a new game
      const params = {
        room: this.room,
      };
      this.$socket.emit('regenerate', params);
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
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
