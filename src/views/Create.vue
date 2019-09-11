<template>
  <v-layout align-center justify-center text-xs-center row wrap mb-5>
    <v-flex sm6 xs12>
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
