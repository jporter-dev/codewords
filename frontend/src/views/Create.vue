<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="8" lg="6" xl="6" align="center" justify="center">
        <v-row>
          <v-col class="py-1">
            <v-avatar tile size="128" v-if="$vuetify.breakpoint.mdAndUp">
              <img src="@/assets/logo-256x256.png" alt="codenames logo" />
            </v-avatar>
            <h1 class="cn-text">{{ $t('title') }}</h1>
            <create-form></create-form>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="py-1">
            <v-btn block color="secondary" large to="home">{{ $t('back') }}</v-btn>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapMutations } from "vuex";
import CreateForm from "@/components/CreateForm";

export default {
  name: "Create",
  components: {
    CreateForm
  },
  mounted() {
    this.reset_error();
  },
  methods: {
    ...mapMutations(["reset_error"])
  }
};
</script>
