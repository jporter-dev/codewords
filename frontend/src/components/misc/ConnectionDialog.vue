<template>
  <v-dialog
    :value="disconnected"
    persistent
    max-width="300px"
    overlay-opacity=".75"
    overlay-color="black"
  >
    <v-card>
      <v-card-title>Connection to server lost...</v-card-title>
      <v-card-text>
        <v-progress-linear
          indeterminate
          color="white"
          class="mb-0"
        ></v-progress-linear>
        Please stand by...
      </v-card-text>
      <v-card-actions>
        <v-btn
          block
          color="red darken-2"
        >
          Report an issue
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState(["disconnected"])
  }
};
</script>

<style>
</style>
