<template>
  <v-layout align-center justify-center text-xs-center row wrap>
    <v-flex sm8 xs12>
      <v-avatar tile size="128">
        <img src="@/assets/logo-256x256.png" alt="codenames logo">
      </v-avatar>
      <h1 class="cn-text">Codewords</h1>
      <v-btn block color="secondary" large to="create" id="create-btn">Create Game</v-btn>
      <join-form></join-form>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapMutations } from 'vuex';
import CreateForm from '@/components/CreateForm';
import JoinForm from '@/components/JoinForm';

export default {
  name: 'Home',
  components: {
    CreateForm,
    JoinForm,
  },
  mounted() {
    this.reset_error();
  },
  methods: {
    ...mapMutations(['reset_error']),

  },
};
</script>
