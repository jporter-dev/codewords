<template>
  <v-row>
    <v-col>
      <v-row no-gutters>
        <v-col>
          <v-switch
            :label="$t('use custom wordbank')"
            v-model="useCustom"
            hide-details
          ></v-switch>
          <v-switch
            v-show="!useCustom"
            :label="$t('mix dictionaries')"
            v-model="mix"
            hide-details
          ></v-switch>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-textarea
            filled
            v-show="useCustom"
            name="custom-wordbank"
            :label="$t('custom wordbank')"
            v-model="rawWordbank"
            :rules="wordbankRules"
            :placeholder="$t('wordbank directions')"
          ></v-textarea>
        </v-col>
      </v-row>

      <v-row>
        <v-col>
          <v-select
            v-show="!useCustom"
            v-model="selectedDictionaries"
            :items="Object.keys(dictionaries)"
            :multiple="mix"
            :menu-props="{'max-height': 400}"
            :label="$t('dictionary')"
            :placeholder="$t('select...')"
            :hint="$t('select a dictionary')"
            persistent-hint
            @change="setMixes"
          ></v-select>

        </v-col>
      </v-row>
      <v-row no-gutters v-show="mix && typeof selectedDictionaries === 'object' && selectedDictionaries && selectedDictionaries.length > 1"
        v-for="(val, dict) in mixes"
        :key="dict"
      >
        <v-col>
          <v-slider
            v-model="mixes[dict]"
            :hint="dict"
            step="5"
            :label="percent(mixPercentages[dict])"
            persistent-hint
          >
          </v-slider>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "DictionaryMixer",
  data() {
    return {
      mix: false,
      selectedDictionaries: "English",
      mixes: {},
      useCustom: false,
      rawWordbank: "",
      wordbankRules: [
        () =>
          (this.wordbank && this.wordbank.length >= 25) ||
          "Word bank must contain at least 25 words."
      ]
    };
  },
  watch: {
    mix(v) {
      this.selectedDictionaries = v ? [] : "English";
    },
    dictionaryOptions: {
      handler: function() {
        this.$emit("setDictionaryOptions", this.dictionaryOptions);
      },
      immediate: true
    }
  },
  computed: {
    ...mapState(["dictionaries"]),
    dictionaryOptions() {
      return {
        mix: this.mix,
        useCustom: this.useCustom,
        dictionaries: this.selectedDictionaries,
        mixPercentages: this.mixPercentages,
        customWordbank: this.wordbank
      };
    },
    // get total of dict sliders
    mixTotal() {
      return this.mix &&
        this.selectedDictionaries &&
        this.selectedDictionaries.length > 0
        ? Object.values(this.mixes)
            .map(val => val || 0) // default values to 0
            .reduce((a, b) => {
              return a + b;
            }, 0)
        : 0; // sum values
    },
    // map dicts to % of total
    mixPercentages() {
      let that = this;
      return Object.keys(that.mixes).reduce(function(obj, key) {
        obj[key] = Math.round((that.mixes[key] * 100) / that.mixTotal) || 0;
        return obj;
      }, {});
    },
    wordbank() {
      // return wordbank split on commas and newlines and uniqued
      return [...new Set(this.rawWordbank.split(/[\n,]/))].filter(String);
    }
  },
  methods: {
    // initialize dict mixes
    setMixes(dicts) {
      if (this.mix) {
        Object.keys(this.mixes).forEach(dict => {
          if (!dicts.includes(dict)) {
            this.$delete(this.mixes, dict);
          }
        });
        dicts.forEach(dict => {
          this.$set(this.mixes, dict, this.mixes[dict] || 50);
        });
      }
    },
    percent(pct) {
      return pct.toString() + "%";
    }
  },
  created() {
    this.$socket.emit("list_dictionaries");
  }
};
</script>

<i18n src="@/plugins/translations/create.json"/>