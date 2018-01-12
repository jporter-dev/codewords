<template>
  <v-layout align-center row wrap mb-5>
    <v-flex sm8 offset-sm2 xs12>
      <img src="/static/images/secret-agent-64-grey.png" alt="codenames" height="64">
      <v-btn block color="secondary" large to="create">Create Game</v-btn>
      <v-slide-y-transition>
        <create-form v-if="showCreate"></create-form>
      </v-slide-y-transition>
      <join-form v-if="!showCreate"></join-form>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapMutations } from 'vuex';
import CreateForm from '@/components/ui/CreateForm';
import JoinForm from '@/components/ui/JoinForm';

export default {
  name: 'Home',
  components: {
    CreateForm,
    JoinForm,
  },
  data() {
    return {
      showCreate: false,
    };
  },
  mounted() {
    this.reset_error();
  },
  methods: {
    ...mapMutations(['reset_error']),

  },
};
</script>