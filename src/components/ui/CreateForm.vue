<template>
  <v-card>
    <v-card-text>
      <v-form @submit="createGame">
        <!-- <v-text-field label="Username" v-model="username" required></v-text-field> -->
        <v-select v-bind:items="dictionaries" v-model="dictionary" label="Dictionary" required dark></v-select>
        <v-radio-group v-model="teams" row label="Teams">
          <v-radio label="2 teams" value="2" ></v-radio>
          <v-radio label="3 teams" value="3"></v-radio>
        </v-radio-group>
        <v-radio-group v-model="size" row label="Board Size">
          <v-radio label="Normal" value="normal" ></v-radio>
          <v-radio label="Large" value="large"></v-radio>
        </v-radio-group>

        <v-btn block color="primary" large @click.stop="createGame">Create</v-btn>
      </v-form @click="createGame">
    </v-card-text>
  </v-card>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'create-form',
  data() {
    return {
      // username: 'unknown',
      dictionaries: ['Simple', 'CAH', 'Standard', 'Pop Culture', 'French'],
      dictionary: 'Simple',
      teams: '2',
      size: 'normal',
    };
  },
  computed: {
    ...mapState(['room']),
  },
  watch: {
    room() {
      this.set_room(this.room);
      this.$router.push({ name: 'Player', params: { room: this.room } });
    },
  },
  methods: {
    ...mapMutations(['set_username', 'set_room']),
    createGame() {
      const params = {
        // username: this.username,
        dictionary: this.dictionary,
        teams: this.teams,
        size: this.size,
      };
      this.set_username(this.username);
      this.$socket.emit('create', params);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
