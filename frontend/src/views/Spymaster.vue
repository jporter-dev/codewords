<template>
  <v-container v-if="!spymasterReveal" fill-height>
    <v-row class="fill-height" align="center" justify="center">
      <v-col cols="12" sm="8" xs="12">
        <v-alert outlined type="warning" :value="true">
          <b>Warning!</b> There should only be two spymasters per game.
        </v-alert>
        <v-btn block large color="success" @click="reveal_spymaster" id="spymaster-btn">I understand. Make me a spymaster!</v-btn>
      </v-col>
    </v-row>
  </v-container>

  <game-board :role="role" v-else></game-board>
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
    ...mapMutations(['set_room', 'reveal_spymaster', 'forget_spymaster']),
  },
  mounted() {
    if (!this.room) this.set_room(this.$route.params.room);
    const params = {
      room: this.room,
    };
    this.$socket.emit('join', params);
  },
  destroyed () {
    this.forget_spymaster()
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
