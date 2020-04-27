<template>
  <v-dialog
    v-model="showDialog"
    max-width="450"
    persistent
  >
    <v-form
      ref="form"
      v-model="valid"
      @submit.prevent="submit"
    >
      <v-card class="telegram">
        <v-card-title>Enter Agent Name</v-card-title>
        <v-card-text>
          <v-text-field
            solo
            v-model="currentUsername"
            :rules="[rules.required]"
          >
          </v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-btn
            block
            color="primary"
            type="submit"
          >Join Game</v-btn>
        </v-card-actions>
      </v-card>
    </v-form>

  </v-dialog>
</template>

<script>
import { mapState, mapGetters, mapMutations } from "vuex";
export default {
  data() {
    return {
      valid: false,
      showDialog: false,
      currentUsername: ""
    };
  },
  computed: {
    ...mapState(["room", "rules"]),
    ...mapGetters(["username"])
  },
  methods: {
    ...mapMutations(["set_username"]),
    submit() {
      this.$refs.form.validate();
      if (this.valid) {
        this.set_username(this.currentUsername);
        const params = {
          username: this.username,
          room: this.room
        };
        this.$socket.emit("join", params);
        this.showDialog = false;
      }
    }
  },
  created() {
    if (!this.$store.state.username) {
      this.showDialog = true;
    }
  },
  mounted() {
    this.currentUsername = this.$store.getters.username;
    let unwatch = this.$watch("$store.getters.username", () => {
      this.currentUsername = this.$store.getters.username;
      unwatch()
    });
  }
};
</script>

<style>
</style>
