<template>
  <game-board :role="role"></game-board>
</template>

<script>
import GameBoard from '@/components/GameBoard';
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'player',
  components: {
    GameBoard,
  },
  computed: {
    ...mapState(['room', 'username']),
    role() {
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
    ...mapMutations(['set_room', 'set_username']),
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
