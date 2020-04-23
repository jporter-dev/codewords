<template>
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
    <span class="grey--text text--darken-4">
      {{spymaster}} - {{!isSpymaster}}
    </span>
  </spymaster-warning>
  <game-board
    :role="role"
    v-else
  ></game-board>
</template>

<script>
import GameBoard from "@/components/game/Board";
import SpymasterWarning from "@/components/game/SpymasterWarning";
import { mapState, mapGetters, mapMutations } from "vuex";

export default {
  name: "player",
  components: {
    GameBoard,
    SpymasterWarning
  },
  props: ["spymaster"],
  computed: {
    ...mapState(["room", "spymasterReveal", "game", "connected", "error"]),
    ...mapGetters(["username", "isSpymaster"]),
    role() {
      if (this.spymaster && !this.spymasterReveal) {
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
          const params = {
            username: this.username,
            room: this.room
          };
          this.$socket.emit("join", params);
          this.setSpymaster();
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
    spymasterReveal: {
      handler() {
        this.setSpymaster();
      }
    },
    isSpymaster: {
      handler(to, from) {
        if (from) this.forget_spymaster();
        this.setSpymaster();
      }
    },
    // reset spymaster if user switches back to agent away
    spymaster(to, from) {
      if (from) this.forget_spymaster();
    }
  },
  destroyed() {
    // reset room and spymaster value when navigating away
    this.reset_room();
    this.$socket.emit("leave_room", { room: this.room });
  },
  methods: {
    ...mapMutations(["set_room", "reset_room", "forget_spymaster"]),
    setSpymaster() {
      const params = {
        room: this.room,
        state: this.spymasterReveal
      };
      this.$socket.emit("toggle_spymaster", params);
    }
  }
};
</script>
