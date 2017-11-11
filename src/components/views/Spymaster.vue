<template>
  <v-card>
    <v-card-text>
      {{ game }}
    </v-card-text>
  </v-card>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'player',
  computed: {
    ...mapState(['game']),
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
