<template>
  <v-container
    fluid
    fill-height
    px-2
    py-0
  >
    <v-app-bar
      app
      fixed
    >
    </v-app-bar>
    <div class="d-flex flex-grow-1 flex-column fill-height">
      <v-row
        v-for="i in 5"
        :key="i"
      >
        <v-col
          v-for="j in 5"
          :key="j"
        >
          <v-card class="fill-height"></v-card>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
export default {};
</script>

<style>
</style>
