<template>
  <v-fade-transition appear>
    <v-form @submit="createGame" id="create-form">
      <v-card>
        <v-card-text>
            <dictionary-mixer @setDictionaryOptions="setDictionaryOptions"></dictionary-mixer>
            <v-row>
              <v-col class="py-1">
                <v-expansion-panels flat>
                  <v-expansion-panel>
                    <v-expansion-panel-header class="pa-1">Advanced Options</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-row>
                        <v-col>
                          <v-radio-group v-model="teams" label="Teams">
                            <v-radio label="2 teams" value="2" ></v-radio>
                            <v-radio label="3 teams" value="3"></v-radio>
                          </v-radio-group>
                        </v-col>
                        <v-col>
                          <v-radio-group v-model="size" label="Board Size">
                            <v-radio label="Normal" value="normal" ></v-radio>
                            <v-radio label="Large" value="large"></v-radio>
                          </v-radio-group>
                        </v-col>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </v-col>
            </v-row>
        </v-card-text>
        <v-card-actions>
          <v-btn block color="primary" large @click="createGame" :disabled="!valid" id="create-btn">Create</v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
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
    ...mapMutations(['set_username', 'set_room', 'reset_room']),
    createGame() {
      this.reset_room();
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
