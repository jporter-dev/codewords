<template>
  <div style="width: 100%;">
    <v-layout align-center justify-center text-xs-center row wrap mb-5 v-if="!spymasterReveal">
      <v-flex sm8 xs12>
        <v-alert outline type="warning" :value="true">
          <b>Warning!</b> There should only be two spymasters per game.
        </v-alert>
        <v-btn block large color="success" @click="reveal_spymaster">I understand. Make me a spymaster!</v-btn>
      </v-flex>
    </v-layout>
    <game-board :role="role" v-if="role !== 'spymaster' || (role === 'spymaster' && spymasterReveal)"></game-board>
  </div>
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
    ...mapState(['room', 'username', 'spymasterReveal']),
    role() {
      if (this.$route.name.toLowerCase() === 'spymaster' && !this.spymasterReveal) {
        return null;
      }
      return this.$route.name;
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
    ...mapMutations(['set_room', 'set_username', 'reveal_spymaster']),
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
