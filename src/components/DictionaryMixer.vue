<template>
  <v-layout row wrap>
    <v-flex xs12>
      <v-switch
        label="Use a custom wordbank"
        v-model="useCustom"
      ></v-switch>
      <v-switch
        v-show="!useCustom"
        label="Mix Dictionaries"
        v-model="mix"
      ></v-switch>
      <v-text-field
        v-show="useCustom"
        name="custom-wordbank"
        label="Custom Wordbank"
        multi-line
        v-model="rawWordbank"
        :rules="wordbankRules"
        placeholder="Enter a comma or newline separated list of words."
      ></v-text-field>
      <v-select
        v-show="!useCustom"
        v-model="selectedDictionaries"
        :items="dictionaries"
        :multiple="mix"
        max-height="400"
        label="Dictionary"
        placeholder="Select..."
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
        :label="mixPercentages[dict]"
        persistent-hint
        >
      </v-slider>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "DictionaryMixer",
  data () {
    return {
      mix: true,
      dictionaries: ['Standard', 'CAH', 'German', 'French'],
      selectedDictionaries: [],
      mixes: {},
      useCustom: false,
      rawWordbank: '',
      wordbankRules: [
        () => (this.wordbank && this.wordbank.length >= 25) || 'Word bank must contain at least 25 words.',
      ],
    }
  },
  watch: {
    dictionaryOptions: {
      handler: function () { this.$emit('setDictionaryOptions', this.dictionaryOptions) },
      immediate: true
    }
  },
  computed: {
    dictionaryOptions () {
      return {
        mix: this.mix,
        useCustom: this.useCustom,
        selectedDictionaries: this.selectedDictionaries,
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
        obj[key] = (Math.floor((that.mixes[key] * 100) / that.mixTotal) || 0).toString() + "%"
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
      dicts.forEach((dict) => {
        this.$set(this.mixes, dict, 50)
      })
    }
  }
}
</script>
