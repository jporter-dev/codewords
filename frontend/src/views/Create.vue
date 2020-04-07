<template>
  <v-layout align-start justify-center text-xs-center row wrap>
    <v-flex lg4 md5 sm6 xs12>
      <v-avatar tile size="128">
        <img src="@/assets/logo-256x256.png" alt="codenames logo">
      </v-avatar>
      <h1 class="cn-text">Codewords</h1>
      <create-form></create-form>
      <v-btn block color="secondary" large to="home">Back</v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapMutations } from 'vuex';
import CreateForm from '@/components/CreateForm';

export default {
  name: 'Create',
  components: {
    CreateForm,
  },
  mounted() {
    this.reset_error();
  },
  methods: {
    ...mapMutations(['reset_error']),

  },
};
</script>
