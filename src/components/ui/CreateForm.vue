<template>
  <v-card>
    <v-card-text>
      <v-form @submit="createGame" v-model="valid">
        <!-- <v-text-field label="Username" v-model="username" required></v-text-field> -->
        <v-switch v-model="useCustom" dark label="Use a custom work bank"></v-switch>
        <v-select v-bind:items="dictionaries" v-model="dictionary" label="Dictionary" required dark v-if="!useCustom"></v-select>
        <v-text-field
          name="custom-wordbank"
          label="Custom Wordbank"
          multi-line
          v-model="rawWordbank"
          :rules="wordbankRules"
          placeholder="Enter a comma or newline separated list of words."
          v-if="useCustom"
        ></v-text-field>
        <v-radio-group v-model="teams" row label="Teams">
          <v-radio label="2 teams" value="2" ></v-radio>
          <v-radio label="3 teams" value="3"></v-radio>
        </v-radio-group>
        <v-radio-group v-model="size" row label="Board Size">
          <v-radio label="Normal" value="normal" ></v-radio>
          <v-radio label="Large" value="large"></v-radio>
        </v-radio-group>

        <v-btn block color="primary" large @click.stop="createGame" :disabled="!valid">Create</v-btn>
      </v-form>
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
      valid: true,
      useCustom: false,
      rawWordbank: '',
      wordbankRules: [
        () => (this.wordbank && this.wordbank.length >= 25) || 'Word bank must contain at least 25 words.',
      ],
    };
  },
  computed: {
    ...mapState(['room']),
    wordbank() {
      // return wordbank split on commas and newlines
      return this.rawWordbank.split(/[\n,]/);
    },
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
        teams: this.teams,
        size: this.size,
      };
      if (this.useCustom) {
        params.wordbank = this.wordbank;
      } else {
        params.dictionary = this.dictionary;
      }
      this.set_username(this.username);
      this.$socket.emit('create', params);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
