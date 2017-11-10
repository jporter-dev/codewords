<template>
  <v-card>
    <v-card-text>
      <v-text-field
        label="Username"
        v-model="username"
      ></v-text-field>
      <v-select
        v-bind:items="dictionaries"
        v-model="dictionary"
        label="Dictionary"
        dark
      ></v-select>
      <v-radio-group v-model="teams" row label="Teams">
        <v-radio label="2 teams" value="2" ></v-radio>
        <v-radio label="3 teams" value="3"></v-radio>
      </v-radio-group>
      <v-radio-group v-model="size" row label="Board Size">
        <v-radio label="Normal" value="normal" ></v-radio>
        <v-radio label="Large" value="large"></v-radio>
      </v-radio-group>

      <v-btn block color="accent" large @click="createRoom">Create</v-btn>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'create-form',
  data() {
    return {
      username: '',
      dictionaries: ['Simple', 'CAH', 'Standard', 'Extended'],
      dictionary: 'Simple',
      teams: '2',
      size: 'normal',
    };
  },
  methods: {
    createRoom() {
      const params = {
        username: this.username,
        dictionary: this.dictionary,
        teams: this.teams,
        size: this.size,
      };
      this.$socket.emit('create', params)
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
