<template>
  <v-fade-transition appear>
    <v-card>
      <v-card-text>
        <v-form @submit="createGame" v-model="valid" id="create-form">
          <v-layout row wrap>
            <v-flex xs12>
              <v-radio-group v-model="dictionaryType" row label="Dictionary Selection">
                <v-radio label="Default" value="single" ></v-radio>
                <v-radio label="Custom" value="custom" ></v-radio>
                <v-radio label="Mixer" value="mixer" ></v-radio>
              </v-radio-group>
            </v-flex>
            <v-flex xs12>
              <v-select v-bind:items="dictionaries" v-model="dictionary" label="Dictionary" required v-if="dictionaryType === 'single'"></v-select>
              <v-text-field
                name="custom-wordbank"
                label="Custom Wordbank"
                multi-line
                v-model="rawWordbank"
                :rules="wordbankRules"
                placeholder="Enter a comma or newline separated list of words."
                v-if="dictionaryType === 'custom'"
              ></v-text-field>
              <dictionary-mixer v-if="dictionaryType === 'mixer'"></dictionary-mixer>
            </v-flex>
            <v-flex xs6>
              <v-radio-group v-model="teams" label="Teams">
                <v-radio label="2 teams" value="2" ></v-radio>
                <v-radio label="3 teams" value="3"></v-radio>
              </v-radio-group>
            </v-flex>
            <v-flex xs6>
              <v-radio-group v-model="size" label="Board Size">
                <v-radio label="Normal" value="normal" ></v-radio>
                <v-radio label="Large" value="large"></v-radio>
              </v-radio-group>
            </v-flex>
            <v-flex xs12>
              <v-btn block color="primary" large @click.stop="createGame" :disabled="!valid" id="create-btn">Create</v-btn>
            </v-flex>
          </v-layout>
        </v-form>
      </v-card-text>
    </v-card>
  </v-fade-transition>
</template>

<script>
import DictionaryMixer from '@/components/DictionaryMixer'
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'create-form',
  components: { DictionaryMixer },
  data() {
    return {
      // username: 'unknown',
      dictionary: 'Simple',
      teams: '2',
      size: 'normal',
      valid: true,
      dictionaryType: 'single',
      rawWordbank: '',
      wordbankRules: [
        () => (this.wordbank && this.wordbank.length >= 25) || 'Word bank must contain at least 25 words.',
      ],
    };
  },
  computed: {
    ...mapState(['room', 'dictionaries']),
    wordbank() {
      // return wordbank split on commas and newlines and uniqued
      return [...new Set(this.rawWordbank.split(/[\n,]/))].filter(String);
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
      if (this.dictionaryType === 'custom') {
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
