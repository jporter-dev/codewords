<template>
  <v-snackbar
    v-model="show"
    :timeout="2500"
    :color="color"
  >
    {{ text }}
    <v-btn
      text
      @click="show = false"
    >
      Close
    </v-btn>
  </v-snackbar>
</template>

<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      show: false,
      color: "",
      text: ""
    };
  },
  computed: {
    ...mapState(["game"])
  },
  watch: {
    "game.players.spymasters": {
      handler(to, from) {
        // add a spymaster
        if (to && from) {
          if (to.length > from.length) {
            let name = to.filter(n => !from.includes(n));
            name = name.map(n => this.game.players.players[n]);

            this.color = "blue darken-2";
            this.text = `${name} became a spymaster`;
            this.show = true;
          } else if (to.length < from.length) {
            let name = from.filter(n => !to.includes(n));
            name = name.map(n => this.game.players.players[n]);

            this.color = "red darken-2";
            this.text = `${name} gave up spymaster`;
            this.show = true;
          }
        }
      }
    }
  }
};
</script>

<style>
</style>
