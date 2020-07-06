<template>
  <v-card :color="colors.background" class="fill-height cn-card telegram" raised tile>
    <slot name="title"></slot>
    <v-card-text class="fill-height pa-1" :class="colors.font">
      <div class="d-flex flex-column fill-height">
        <div
          class="d-flex flex-grow-1 align-center justify-center text-center cn-word py-3 cn-text cn-text--upcase"
          v-resize-text="{ratio: 1.1, minFontSize, maxFontSize}"
        >{{word}}</div>
        <div
          class="d-flex flex-shrink-1 align-end justify-end cn-team"
          v-if="$vuetify.breakpoint.mdAndUp"
        >
          <h6
            class="cn-text cn-text--upcase"
            v-resize-text="{maxFontSize: 16, minFontSize: 12, ratio: 2}"
          >{{getTeamName(team)}}</h6>
        </div>
      </div>
    </v-card-text>
    <slot name="actions"></slot>
  </v-card>
</template>

<script>
export default {
  props: ["word", "team", "colors"],
  computed: {
    minFontSize() {
      return this.$vuetify.breakpoint.mdAndUp ? 20 : 18;
    },
    maxFontSize() {
      return this.$vuetify.breakpoint.mdAndUp ? 30 : 24;
    }
  },
  methods: {
    getTeamName(team) {
      switch (team) {
        case "R":
          return `$t("red")`;
        case "B":
          return `$t("blue")`;
        case "G":
          return `$t("green")`;
        case "O":
          return `$t("citizen")`;
        case "X":
          return `$t("assassin")`;
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
  font-family: "Courier New", Courier, "Lucida Sans Typewriter",
    "Lucida Typewriter", monospace !important;
  font-weight: bold;
}

.cn-card.dialog-card .cn-team {
  display: none !important;
}

.cn-card.dialog-card .cn-word {
  min-height: 100px;
}

.cn-team {
  position: absolute;
  bottom: 0;
  right: 0;
}
</style>

<i18n src="@/plugins/translations/game.json"/>