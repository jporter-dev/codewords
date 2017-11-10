<template>
  <v-layout row wrap>
    <v-flex sm8 offset-sm2 xs12>
      <join-form v-if="!showCreate"></join-form>
      <v-btn block color="secondary" large @click="showCreate = !showCreate">Create Game</v-btn>
      <create-form v-if="showCreate"></create-form>
    </v-flex>
  </v-layout>
</template>

<script>
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
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar.is-fixed-top { position: fixed !important; top: 0; left: 0; right: 0; z-index: 1; }
.navbar.is-fixed-bottom { position: fixed !important; bottom: 0; left: 0; right: 0; z-index: 1; }
</style>
