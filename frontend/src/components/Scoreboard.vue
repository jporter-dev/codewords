<template>
  <div v-if="tileCounts">
    <span class="red--text text--darken-1">{{tileCounts.total.R - tileCounts.flipped.R}}</span>
    <span
      style="padding: 0 10px;"
      v-if="!'G' in tileCounts.flipped"
    >
      <v-avatar size="32">
        <img
          src="@/assets/logo-64x64.png"
          alt="codenames logo"
        />
      </v-avatar>
    </span>
    <span v-else> - </span>
    <span class="blue--text text--lighten-2">{{tileCounts.total.B - tileCounts.flipped.B}}</span>
    <template v-if="'G' in tileCounts.flipped">
      <span> - </span>
      <span class="green--text text--lighten-1">{{tileCounts.total.R - tileCounts.flipped.G}}</span>
    </template>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
export default {
  computed: {
    ...mapGetters(['tileCounts'])
  }
};
</script>
