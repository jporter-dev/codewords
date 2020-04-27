<template>
  <v-container
    class="align-start"
    fill-height
    fluid
    ma-0
    pa-0
  >
    <username-prompt></username-prompt>
    <v-container v-if="error">
      <v-alert
        type="error"
        prominent
        text
        outlined
      >
        <v-row
          align="center"
          dense
        >
          <v-col class="grow">{{error}}</v-col>
          <v-col
            class="shrink"
            v-if="$vuetify.breakpoint.smAndUp"
          >
            <v-btn
              to="/"
              block
            >
              Go Home
            </v-btn>
          </v-col>
        </v-row>
        <v-row
          dense
          v-if="$vuetify.breakpoint.xs"
        >
          <v-col>
            <v-btn
              to="/"
              block
            >
              Go Home
            </v-btn>
          </v-col>
        </v-row>
      </v-alert>
    </v-container>
    <spymaster-warning v-else-if="spymaster && !isSpymaster">
    </spymaster-warning>
    <game-board
      :role="role"
      v-else
    ></game-board>
  </v-container>

</template>

<script>
import GameBoard from "@/components/game/Board";
import SpymasterWarning from "@/components/game/SpymasterWarning";
import UsernamePrompt from "@/components/misc/UsernamePrompt";
import { mapState, mapGetters, mapMutations } from "vuex";

export default {
  name: "player",
  components: {
    GameBoard,
    SpymasterWarning,
    UsernamePrompt
  },
  props: ["spymaster"],
  computed: {
    ...mapState(["room", "game", "connected", "error"]),
    ...mapGetters(["username", "isSpymaster"]),
    role() {
      if (this.spymaster && !this.isSpymaster) {
        return null;
      }
      return this.$route.name;
    }
  },
  watch: {
    // connect to room when WS connection established
    connected: {
      immediate: true,
      handler() {
        if (this.connected) {
          this.set_room(this.$route.params.room);
          if (this.$store.state.username) {
            const params = {
              username: this.username,
              room: this.room
            };
            this.$socket.emit("join", params);
          }
        }
      }
    },
    "$route.params.room": {
      immediate: true,
      handler() {
        this.reset_room();
        this.set_room(this.$route.params.room);
      }
    },
    isSpymaster: {
      handler(to, from) {
        if (from) this.forgetSpymaster();
      }
    },
    // reset spymaster if user switches back to agent away
    spymaster(to, from) {
      if (from) this.forgetSpymaster();
    }
  },
  destroyed() {
    // reset room and spymaster value when navigating away
    this.reset_room();
    this.$socket.emit("leave_room", { room: this.room });
  },
  methods: {
    ...mapMutations(["set_room", "reset_room"]),
    forgetSpymaster() {
      if (this.isSpymaster)
        this.$socket.emit("toggle_spymaster", {
          room: this.room,
          state: false
        });
      if (this.$route.name !== "Player")
        this.$router.push({
          name: "Player",
          params: {
            room: this.room
          }
        });
    }
  }
};
</script>
