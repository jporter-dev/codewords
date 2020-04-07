<template>
  <v-fade-transition appear>
    <v-card>
      <v-card-text>
        <v-form @submit="createGame" id="create-form">
          <v-layout row wrap>
            <v-flex xs12>
              <dictionary-mixer @setDictionaryOptions="setDictionaryOptions"></dictionary-mixer>
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
              <v-btn block color="primary" large @click="createGame" :disabled="!valid" id="create-btn">Create</v-btn>
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
      teams: '2',
      size: 'normal',
      valid: true,
      dictionaryOptions: {},
      errors: []
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
        teams: this.teams,
        size: this.size,
        dictionaryOptions: this.dictionaryOptions
      };
      this.set_username(this.username);
      if (this.valid) {
        this.$socket.emit('create', params);
      } else {
        this.errors.push('Please select a dictionary.')
      }
    },
    setDictionaryOptions (opts) {
      this.dictionaryOptions = opts
      this.valid = (!opts.useCustom && opts.dictionaries && opts.dictionaries.length > 0) ||
        (opts.useCustom && opts.customWordbank && opts.customWordbank.length >= 25)
    }
  },
};
</script>
