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
    <v-flex v-if="mix" xs12 v-for="dict in selectedDictionaries" :key="dict">
      <v-slider v-model="mixes[dict]" :hint="dict" persistent-hint thumb-label step="10" ticks></v-slider>
    </v-flex>
    {{selectedDictionaries}}
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
}
</script>
