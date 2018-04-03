<template>
  <v-layout align-center justify-center text-xs-center row wrap>
    <v-flex sm8 xs12>
      <img src="@/assets/secret-agent-64-grey.png" alt="codenames" height="64">
      <v-btn block color="secondary" large to="create">Create Game</v-btn>
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
