<template>
  <v-layout row wrap>
    <v-flex xs12>
      <v-switch
        label="Use a custom wordbank"
        v-model="useCustom"
        hide-details
      ></v-switch>
      <v-switch
        v-show="!useCustom"
        label="Mix Dictionaries (Beta)"
        v-model="mix"
        hide-details
      ></v-switch>
      <v-textarea
        box
        v-show="useCustom"
        name="custom-wordbank"
        label="Custom Wordbank"
        v-model="rawWordbank"
        :rules="wordbankRules"
        placeholder="Enter a comma or newline separated list of words."
      ></v-textarea>
      <v-select
        v-show="!useCustom"
        v-model="selectedDictionaries"
        :items="dictionaries"
        :multiple="mix"
        :menu-props="{'max-height': 400}"
        label="Dictionary"
        placeholder="Select..."
        hint="Select a dictionary"
        persistent-hint
        @change="setMixes"
      ></v-select>
    </v-flex>
    <v-flex
      v-show="mix && typeof selectedDictionaries === 'object' && selectedDictionaries && selectedDictionaries.length > 1"
      xs12
      v-for="(val, dict) in mixes" :key="dict">
      <v-slider v-model="mixes[dict]"
        :hint="dict"
        step="5"
        :label="percent(mixPercentages[dict])"
        persistent-hint
        >
      </v-slider>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapState} from 'vuex';

export default {
  name: "DictionaryMixer",
  data () {
    return {
      mix: false,
      selectedDictionaries: 'English',
      mixes: {},
      useCustom: false,
      rawWordbank: '',
      wordbankRules: [
        () => (this.wordbank && this.wordbank.length >= 25) || 'Word bank must contain at least 25 words.',
      ],
    }
  },
  watch: {
    mix (v) {
      this.selectedDictionaries = v ? [] : 'English';
    },
    dictionaryOptions: {
      handler: function () { this.$emit('setDictionaryOptions', this.dictionaryOptions) },
      immediate: true
    }
  },
  computed: {
    ...mapState(['dictionaries']),
    dictionaryOptions () {
      return {
        mix: this.mix,
        useCustom: this.useCustom,
        dictionaries: this.selectedDictionaries,
        mixPercentages: this.mixPercentages,
        customWordbank: this.wordbank
      }
    },
    // get total of dict sliders
    mixTotal () {
      return (this.mix && this.selectedDictionaries && this.selectedDictionaries.length > 0) ?
        Object.values(this.mixes)
          .map((val) => val || 0) // default values to 0
          .reduce((a, b) => { return a+b }, 0) : 0 // sum values
    },
    // map dicts to % of total
    mixPercentages () {
      let that = this
      return Object.keys(that.mixes).reduce(function(obj, key) {
        obj[key] = (Math.round((that.mixes[key] * 100) / that.mixTotal) || 0)
        return obj;
      }, {});
    },
    wordbank() {
      // return wordbank split on commas and newlines and uniqued
      return [...new Set(this.rawWordbank.split(/[\n,]/))].filter(String);
    },
  },
  methods: {
    // initialize dict mixes
    setMixes (dicts) {
      if (this.mix) {
        Object.keys(this.mixes).forEach((dict) => {
          if (!dicts.includes(dict)) {
            this.$delete(this.mixes, dict)
          }
        })
        dicts.forEach((dict) => {
          this.$set(this.mixes, dict, this.mixes[dict] || 50)
        })
      }
    },
    percent (pct) {
      return pct.toString() + "%"
    }
  }
}
</script>
