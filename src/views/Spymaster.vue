<template>
  <v-layout align-center justify-center text-xs-center mb-5 v-if="!spymasterReveal">
    <v-flex sm8 xs12>
      <v-alert outline type="warning" :value="true">
        <b>Warning!</b> There should only be two spymasters per game.
      </v-alert>
      <v-btn block large color="success" @click="reveal_spymaster" id="spymaster-btn">I understand. Make me a spymaster!</v-btn>
    </v-flex>
  </v-layout>
  <v-layout row wrap v-else>
    <v-flex xs12 fill-height>
      <game-board :role="role" v-if="spymasterReveal">
        <v-btn block large v-if="gameWon" color="success" @click.native="newGame(true)">New Game</v-btn>
        <v-btn block large v-if="isFirstTurn && !gameWon" color="success" @click.native="newGame" id="shuffle-btn">Shuffle New Words</v-btn>
      </game-board>
    </v-flex>
  </v-layout>
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
    ...mapState(['room', 'username', 'spymasterReveal', 'game', 'connected']),
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
    ...mapMutations(['set_room', 'set_username', 'reveal_spymaster', 'reset_room']),
    newGame(reset) {
      // reset spymaster state and go to player view
      // emit message to start a new game
      const params = {
        room: this.room,
      };
      if (reset === true) {
        this.reset_room()
        params['newGame'] = true
        this.$router.push({ path: `/${this.room}/player` })
      }
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
