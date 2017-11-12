<template>
  <v-fade-transition appear>  
    <v-layout row wrap pt-5>
      <v-flex>
        <v-card tile flat dark>
          <v-card-text px-0 class='text-xs-left'>
            <h4 class="header">How to Play</h4>
            <p>Codenames consists of two teams with two roles on each team: a spymaster and field agents.</p>
            <h4 class="subheading">Spymasters</h4>
            <h4 class="subheading">Field Agents</h4>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-fade-transition>
</template>

<script>
export default {
  name: 'help',
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
