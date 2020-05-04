<template>
  <div v-if="game && game.board">
    <v-list-item @click="newGame" :ripple="false" class="green">
      <v-list-item-action>
        <v-icon>mdi-shuffle</v-icon>
      </v-list-item-action>
    </v-list-item>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";

export default {
  computed: {
    ...mapState(["game"])
  },
  methods: {
    ...mapMutations(["reset_room", "new_game"]),
    newGame() {
      this.$store.commit("set_drawer", false);
      this.new_game(false);
    }
  }
};
</script>

<style lang="scss" scoped>
.v-speed-dial {
  bottom: 65px;
  z-index: 999;
}
#show-more {
  bottom: 75px;
}
</style>
