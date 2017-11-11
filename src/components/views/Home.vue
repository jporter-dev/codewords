<template>
  <v-layout row wrap>
    <v-flex sm8 offset-sm2 xs12>
      <img src="/static/images/secret-agent-128.png" alt="codenames" height="64">
      <h1 class="title grey--text">Codenames</h1>
      <v-btn block color="secondary" large @click="showCreate = !showCreate">Create Game</v-btn>
      <create-form transition="slide-y-transition" v-if="showCreate"></create-form>
      <join-form v-if="!showCreate" transition="slide-y-transition"></join-form>
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
