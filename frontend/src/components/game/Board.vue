<template>
  <v-container
    fluid
    fill-height
    px-2
    py-1
    v-if="role && game.board"
  >
    <div class="fill-height d-flex flex-column flex-grow-1">
      <div class="d-flex flex-shrink-1">
        <slot></slot>
      </div>
      <div class="d-flex flex-grow-1 flex-wrap flex-column">
        <v-row
          dense
          v-for="row in gridRows"
          :key="row"
        >
          <v-col
            v-for="cell in gridCells"
            :key="cell"
            @click="showFlipCard(getWord(row, cell))"
          >
            <game-card
              :word="getWord(row, cell)"
              :team="getTeam(getWord(row, cell))"
              :colors="getColor(getWord(row, cell), getTeam(getWord(row, cell)))"
            ></game-card>
          </v-col>
        </v-row>
      </div>
    </div>
    <v-dialog
      v-model="confirmShow"
      max-width="290"
    >
      <game-card
        class="dialog-card"
        :word="confirmCard"
        :team="getTeam(confirmCard)"
        :colors="getColor(confirmCard, getTeam(confirmCard))"
      >
        <template v-slot:actions>
          <v-card-actions>
            <v-btn
              block
              large
              color="secondary"
              @click.stop="flipCard"
            >Confirm</v-btn>
          </v-card-actions>
        </template>
      </game-card>
    </v-dialog>
    <v-snackbar
      color="red darken-3"
      :vertical="true"
      v-model="agentAlert"
    >
      Only the Spymaster can flip cards.
      <v-btn
        text
        :to="{ name: 'Spymaster', params: { room: room }}"
      >Switch to Spymaster</v-btn>
    </v-snackbar>
  </v-container>
  <skeleton v-else></skeleton>
</template>

<script>
import { mapState, mapGetters, mapMutations } from "vuex";
import GameControls from "@/components/game/Controls";
import GameCard from "@/components/game/Card";
import Skeleton from "@/components/game/Skeleton";

export default {
  name: "game-board",
  components: { GameControls, GameCard, Skeleton },
  props: ["role"],
  data() {
    return {
      confirmShow: false,
      confirmCard: null,
      spymaster: "Spymaster",
      agentAlert: false,
      gameBottom: window.screen.height * 2
    };
  },
  computed: {
    ...mapState(["connected", "room", "game"]),
    ...mapGetters(["words", "gameWon", "username"]),
    cards() {
      if (this.isSpymaster()) {
        return this.game.solution;
      }
      return this.game.board;
    },
    gridRows() {
      if (this.words) {
        switch (this.$vuetify.breakpoint.name) {
          // case 'xs': return '1'
          // case 'sm': return '1'
          default:
            return Math.sqrt(this.words.length);
        }
      }
      return 0;
    },
    gridCells() {
      if (this.words) {
        return this.words.length / this.gridRows;
      }
      return 0;
    },
    responsiveClass() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return "body-2";
        case "lg":
          return "display-1";
        case "xl":
          return "display-1";
        default:
          return "headline";
      }
    }
  },
  methods: {
    ...mapMutations(["set_room"]),
    isSpymaster() {
      return this.role === this.spymaster;
    },
    getWord(row, cell) {
      const temp = (row - 1) * this.gridRows + (cell - 1);
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
      let background = "grey darken-3";
      let font = "";
      if (
        !word ||
        (!this.isSpymaster() && this.game.board[word]) ||
        (this.isSpymaster() && !this.game.board[word])
      ) {
        switch (id) {
          case "R":
            background = "red darken-3";
            break;
          case "G":
            background = "green lighten-1";
            break;
          case "B":
            background = "blue darken-2";
            break;
          case "O":
            background = "grey lighten-3";
            font = "black--text";
            break;
          case "X":
            background = "black";
            break;
          case "-":
            background = "grey lighten-4";
            font = "black--text";
            break;
          default:
            background = "";
            break;
        }
      } else if (this.isSpymaster() && this.game.board[word]) {
        switch (id) {
          case "R":
            font = "red--text text--darken-1";
            break;
          case "G":
            font = "green--text text--lighten-1";
            break;
          case "B":
            font = "blue--text text--darken-1";
            break;
          case "O":
            font = "grey--text text--lighten-1";
            break;
          case "X":
            font = "black--text";
            break;
          case "-":
            font = "grey--text text--lighten-1";
            break;
          default:
            background = "";
            break;
        }
      }
      return {
        background,
        font
      };
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
      if (
        this.isSpymaster() &&
        !this.game.board[this.confirmCard] &&
        this.confirmCard
      ) {
        // send request to confirm the card
        const params = {
          card: this.confirmCard,
          room: this.room
        };
        this.$socket.emit("flip_card", params);
        // reset confirmCard
        this.confirmCard = null;
        this.confirmShow = false;
      } else {
        // card already flipped
        this.confirmCard = null;
      }
    }
  }
};
</script>

<style scoped>
#scrollButton {
  bottom: 60px;
  opacity: 0.75;
}
</style>
