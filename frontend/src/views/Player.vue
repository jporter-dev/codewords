<template>
  <v-container v-if="spymaster && !spymasterReveal" fill-height>
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
import GameBoard from '@/components/game/Board';
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'player',
  components: {
    GameBoard,
  },
  props: ['spymaster'],
  computed: {
    ...mapState(['room', 'spymasterReveal', 'game', 'connected']),
    role() {
      if (this.spymaster && !this.spymasterReveal) {
        return null;
      }
      return this.$route.name;
    },
  },
  watch: {
    // connect to room when WS connection established
    connected: {
      immediate: true,
      handler () {
        if (this.connected) {
          const params = {
            room: this.room,
          };
          this.$socket.emit('join', params);
        }
      }
    },
    // reset spymaster if user switches back to agent away
    spymaster (to, from) {
      if(from)
        this.forget_spymaster();
    }
  },
  mounted() {
    // set the room variable to the route param
    if (!this.room) this.set_room(this.$route.params.room);
  },
  destroyed () {
    // reset room and spymaster value when navigating away
    this.reset_room()
  },
  methods: {
    ...mapMutations(['set_room', 'reset_room', 'reveal_spymaster', 'forget_spymaster']),
  },
};
</script>