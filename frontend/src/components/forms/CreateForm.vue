<template>
  <v-fade-transition appear>
    <v-form
      @submit.prevent="createGame"
      id="create-form"
      ref="form"
      v-model="valid"
    >
      <v-card>
        <v-card-text>
          <v-row>
            <v-col>
              <v-text-field
                :label="$t('secret agent name')"
                :placeholder="$t('pick an agent name')"
                v-model="username"
                :rules="[rules.required, rules.name_length]"
                counter="20"
                outlined
              ></v-text-field>
            </v-col>
          </v-row>
          <dictionary-mixer @setDictionaryOptions="setDictionaryOptions"></dictionary-mixer>
          <v-row>
            <v-col class="py-1">
              <v-expansion-panels flat>
                <v-expansion-panel>
                  <v-expansion-panel-header class="pa-1">{{ $t('advanced options') }}</v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <v-row>
                      <v-col>
                        <v-radio-group
                          v-model="teams"
                          :label="$t('teams')"
                        >
                          <v-radio
                            :label="$t('2 teams')"
                            value="2"
                          ></v-radio>
                          <v-radio
                            :label="$t('3 teams')"
                            value="3"
                          ></v-radio>
                        </v-radio-group>
                      </v-col>
                      <v-col>
                        <v-radio-group
                          v-model="size"
                          :label="$t('board size')"
                        >
                          <v-radio
                            :label="$t('normal')"
                            value="normal"
                          ></v-radio>
                          <v-radio
                            :label="$t('large')"
                            value="large"
                          ></v-radio>
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
          <v-btn
            block
            color="primary"
            large
            type="submit"
            id="create-btn"
          >{{ $t('create') }}</v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-fade-transition>
</template>

<script>
import DictionaryMixer from "@/components/DictionaryMixer";
import { mapState, mapMutations } from "vuex";

export default {
  name: "create-form",
  components: { DictionaryMixer },
  data() {
    return {
      teams: "2",
      size: "normal",
      valid: false,
      dictionaryOptions: {},
      errors: []
    };
  },
  computed: {
    ...mapState(["room", "rules"]),
    username: {
      get() {
        return this.$store.state.username;
      },
      set(v) {
        return this.$store.commit("set_username", v);
      }
    }
  },
  watch: {
    room() {
      this.set_room(this.room);
      this.$router.push({ name: "Player", params: { room: this.room } });
    }
  },
  methods: {
    ...mapMutations(["set_username", "set_room", "reset_room"]),
    createGame() {
      this.$refs.form.validate();
      if (this.valid) {
        this.reset_room();
        const params = {
          username: this.$store.getters.username,
          teams: this.teams,
          size: this.size,
          dictionaryOptions: this.dictionaryOptions
        };
        this.set_username(this.username);
        if (this.valid) {
          this.$socket.emit("create", params);
        } else {
          this.errors.push("Please select a dictionary.");
        }
      }
    },
    setDictionaryOptions(opts) {
      this.dictionaryOptions = opts;
      this.valid =
        (!opts.useCustom &&
          opts.dictionaries &&
          opts.dictionaries.length > 0) ||
        (opts.useCustom &&
          opts.customWordbank &&
          opts.customWordbank.length >= 25);
    }
  }
};
</script>

<i18n src="@/plugins/translations/create.json"/>
