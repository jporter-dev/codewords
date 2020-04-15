<template>
  <v-container>
    <v-row justify="center">
      <v-col
        cols="12"
        sm="8"
        md="8"
        lg="6"
        xl="6"
        justify="center"
      >
        <v-row justify="center">
          <v-avatar
            tile
            size="128"
          >
            <img
              src="@/assets/logo-256x256.png"
              alt="codenames logo"
            >
          </v-avatar>
        </v-row>
        <v-row
          align="center"
          justify="center"
        >
          <h1 class="cn-text">{{ $t('codewords') }}</h1>
        </v-row>
        <v-row>
          <v-col class="py-1">
            <v-btn
              block
              color="secondary"
              large
              to="create"
              id="create-btn"
            >
              {{ $t('create game') }}
            </v-btn>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="py-1">
            <join-form></join-form>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="py-1">
            <v-card class="text-xs-left">
              <v-card-title>
                <span class="title font-weight-light">{{ $t('enjoying codewords?')}}</span>
              </v-card-title>
              <v-card-text class="ma-0 py-1">
                {{ $t('consider donating') }}
              </v-card-text>
              <v-card-actions class="text-xs-left">
                <coffee-button></coffee-button>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapMutations } from "vuex";
import JoinForm from "@/components/forms/JoinForm";
import CoffeeButton from "@/components/misc/CoffeeButton";

export default {
  name: "Home",
  components: {
    JoinForm,
    CoffeeButton
  },
  mounted() {
    this.reset_error();
  },
  methods: {
    ...mapMutations(["reset_error"])
  }
};
</script>
