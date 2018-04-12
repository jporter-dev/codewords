<template>
  <v-layout row wrap>
    <v-flex xs12>
      <v-switch
        label="Mix Dictionaries"
        v-model="mix"
      ></v-switch>
      <v-select
        :items="dictionaries"
        v-model="selectedDictionaries"
        :multiple="mix"
        max-height="400"
        label="Select dictionaries to mix"
        persistent-hint
      ></v-select>
    </v-flex>
    <v-flex v-if="mix && typeof selectedDictionaries === 'object'" xs12 v-for="dict in selectedDictionaries" :key="dict">
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
      mix: false,
      dictionaries: ['Standard', 'CAH', 'German', 'French'],
      selectedDictionaries: [],
      mixes: {},
    }
  },
  computed: {
    mixTotal () {
      return (this.mix && this.selectedDictionaries.length > 0) ?
        Object.values(this.mixes)
          .map((val) => val || 0) // default values to 0
          .reduce((a, b) => { return a+b }, 0) : 0 // sum values
    },
    mixPercentages () {
      let that = this
      return Object.keys(that.mixes).reduce(function(obj, key) {
        obj[key] = (Math.floor((that.mixes[key] * 100) / that.mixTotal) || 0).toString() + "%"
        return obj;
      }, {});
    }
  }
}
</script>
