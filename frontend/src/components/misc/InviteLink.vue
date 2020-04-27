<template>
  <div>
    <v-btn
      outlined
      @click="showDialog = true"
    >
      Invite
    </v-btn>
    <v-dialog
      v-model="showDialog"
      max-width="450"
    >
      <v-card class="telegram">
        <v-card-title class="justify-center">Room ID: {{room}}</v-card-title>
        <v-card-text>
          <v-text-field
            solo
            readonly
            :value="currentLink"
            ref="copy"
          >
            <template v-slot:append>
              <v-btn @click="copyRoom">
                Copy
              </v-btn>
            </template>
          </v-text-field>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      showDialog: false,
      currentLink: window.location.href
    };
  },
  computed: {
    ...mapState(["room"])
  },
  watch: {
    showDialog(val) {
      if (val) this.currentLink = window.location.href;
    }
  },
  methods: {
    copyRoom() {
      this.$refs.copy.$refs.input.select();
      document.execCommand("copy");
      this.showDialog = false;
    }
  }
};
</script>

<style>
</style>
