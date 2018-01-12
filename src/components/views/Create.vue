<template>
  <v-layout align-center row wrap mb-5>
    <v-flex sm8 offset-sm2 xs12>
      <img src="/static/images/secret-agent-64-grey.png" alt="codenames" height="64">
      <create-form></create-form>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapMutations } from 'vuex';
import CreateForm from '@/components/ui/CreateForm';

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