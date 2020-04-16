<template>
  <v-fade-transition appear>
    <v-form
      v-model="validForm"
      @submit.prevent="joinGame"
    >
      <v-card>
        <v-card-text>
          <v-alert
            type="error"
            :value="showInputError"
            transition="slide-y-reverse-transition"
          >
            Room ID is required to join.
          </v-alert>
          <v-row
            dense
            class="mb-3"
          >
            <v-col cols="4">
              <v-text-field
                label="Room ID"
                placeholder="Enter a Room ID"
                v-model="room_num"
                :rules="[rules.required]"
                mask="AAAAA"
                outlined
                hide-details
              ></v-text-field>
            </v-col>
            <v-col>
              <v-text-field
                label="Secret Agent Name"
                placeholder="Pick a secret agent name..."
                v-model="username"
                outlined
                hide-details
              ></v-text-field>
            </v-col>
          </v-row>
          <v-btn
            block
            color="primary"
            large
            type="submit"
            @click.stop="joinGame"
          >Join</v-btn>
        </v-card-text>
      </v-card>
    </v-form>
  </v-fade-transition>
</template>

<script>
import { mapState, mapMutations } from "vuex";

export default {
  name: "create-form",
  data() {
    return {
      validForm: false,
      room_num: null,
      showInputError: false
    };
  },
  computed: {
    ...mapState(["rules"]),
    username: {
      get() {
        return this.$store.state.username;
      },
      set(v) {
        return this.$store.commit("set_username", v);
      }
    },
    room_id() {
      return this.room_num.toUpperCase();
    }
  },
  methods: {
    ...mapMutations(["set_username", "set_room"]),
    joinGame() {
      this.showInputError = false;
      if (this.validForm) {
        this.set_room(this.room_id);
        this.$router.push({ name: "Player", params: { room: this.room_id } });
      } else {
        this.showInputError = true;
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
