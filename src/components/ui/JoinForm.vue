<template>
  <v-card>
    <v-card-text>
      <v-text-field
        label="Room ID"
        v-model="room"
        required
        autofocus
      ></v-text-field>
      
      <v-btn block color="primary" large>Join</v-btn>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'create-form',
  data() {
    return {
      room: null,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
