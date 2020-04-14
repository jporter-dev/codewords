<template>
  <v-card
    :color="colors.background"
    class="fill-height cn-card telegram"
    raised
    tile
  >
    <v-card-text
      class="fill-height pa-1"
      :class="colors.font"
    >
      <div class="d-flex flex-column fill-height">
        <div
          class="d-flex flex-grow-1 align-center justify-center text-center cn-word py-3 cn-text cn-text--upcase"
          v-resize-text="{ratio: 1.1}"
        >
          {{word}}
        </div>
        <div
          class="d-flex flex-shrink-1 align-end justify-end cn-team"
          v-if="$vuetify.breakpoint.mdAndUp"
        >
          <h6
            class="cn-text cn-text--upcase"
            v-resize-text="{maxFontSize: 16, minFontSize: 12, ratio: 2}"
          >
            {{getTeamName(team)}}
          </h6>
        </div>
      </div>
    </v-card-text>
    <slot name="actions"></slot>
  </v-card>
</template>

<script>
export default {
  props: ["word", "team", "colors"],
  methods: {
    getTeamName(team) {
      switch (team) {
        case "R":
          return "Red";
        case "B":
          return "Blue";
        case "G":
          return "Green";
        case "O":
          return "Citizen";
        case "X":
          return "Assassin";
        default:
          return "";
      }
    }
  }
};
</script>

<style scoped>
.cn-card {
  cursor: pointer;
  flex-basis: 0;
  flex-shrink: 0;
  flex-grow: 1;
}

.cn-text {
  letter-spacing: 5px !important;
}

.cn-card.dialog-card .cn-team {
  display: none !important;
}

.cn-card.dialog-card .cn-word {
  min-height: 100px;
}
</style>
