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
      <game-board :role="role" v-if="spymasterReveal"></game-board>
    </v-flex>
  </v-layout>
</template>

<script>
import GameBoard from '@/components/GameBoard';
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'spymaster',
  components: {
    GameBoard,
  },
  computed: {
    ...mapState(['room', 'spymasterReveal', 'game', 'connected']),
    role() {
      if (!this.spymasterReveal) {
        return null;
      }
      return this.$route.name;
    },
  },
  methods: {
    ...mapMutations(['set_room', 'reveal_spymaster']),
  },
  mounted() {
    if (!this.room) this.set_room(this.$route.params.room);
    const params = {
      room: this.room,
    };
    this.$socket.emit('join', params);
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
