<template>
  <v-layout
    align-start
    justify-center
    text-xs-center
    row
    wrap
  >
    <v-flex
      lg4
      md5
      sm6
      xs12
    >
      <v-avatar
        tile
        size="128"
        v-if="$vuetify.breakpoint.mdAndUp"
      >
        <img
          src="@/assets/logo-256x256.png"
          alt="codenames logo"
        >
      </v-avatar>
      <h1 class="cn-text cn-text--upcase">Codewords</h1>
      <v-alert
        :value="clients >= 900"
        type="warning"
        outline
        class="text-xs-left"
      >
        Codewords.tv is experiencing a higher than usual load.
        Apologies if the site is down or having issues, please feel free to
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSfLs3pnKu7WifF4WQdq0Q8VAtiY1WARyw8O_rmrxjYnm7Zz1g/viewform?usp=sf_link">report an outage</a>
        or <a href="https://beta.codewords.tv/">try the beta</a>!
      </v-alert>
      <v-alert
        :value="clients < 900"
        type="info"
        outline
        class="text-xs-left"
      >
          Thanks for supporting Codewords.tv! Server stability and new features are being developed over at
          <a href="https://beta.codewords.tv/" class="blue--text text--lighten-4">beta.codewords.tv</a>, feel free to try it out!
      </v-alert>
      <v-btn
        block
        color="secondary"
        large
        to="create"
        id="create-btn"
      >Create Game</v-btn>
      <join-form></join-form>
      <v-card class="mt-2 text-xs-left">
        <v-card-title>
          <span class="title font-weight-light">Enjoying Codewords.tv?</span>
        </v-card-title>
        <v-card-text class="ma-0 py-1">
          Consider donating to keep this website running and to support future development!
        </v-card-text>
        <v-card-actions class="text-xs-left">
          <coffee-button></coffee-button>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapState, mapMutations } from "vuex";
import CreateForm from "@/components/CreateForm";
import JoinForm from "@/components/JoinForm";
import CoffeeButton from "@/components/CoffeeButton";

export default {
  name: "Home",
  components: {
    CreateForm,
    JoinForm,
    CoffeeButton
  },
  computed: {
    ...mapState(["clients"])
  },
  mounted() {
    this.reset_error();
  },
  methods: {
    ...mapMutations(["reset_error"])
  }
};
</script>
