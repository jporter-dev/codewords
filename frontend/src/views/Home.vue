<template>
  <v-container>
    <v-row
      align="center"
      justify="center"
    >
      <v-col
        cols="12"
        sm="8"
        md="8"
        lg="6"
        xl="6"
        align="center"
        justify="center"
      >
        <v-row
          align="center"
          justify="center"
        >
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
import CreateForm from "@/components/CreateForm";
import JoinForm from "@/components/JoinForm";
import CoffeeButton from "@/components/misc/CoffeeButton";
import messages from "@/plugins/translations/en/home.json";
// import common_messages from "@/plugins/translations/en/common.json";

export default {
  name: "Home",
  components: {
    CreateForm,
    JoinForm,
    CoffeeButton
  },
  mounted() {
    this.reset_error();
  },
  methods: {
    ...mapMutations(["reset_error"])
  },
  i18n: {
    messages: messages,
    sharedMessages: common_messages
  }
};
</script>
