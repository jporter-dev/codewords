<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title class="align-center justify-center headline">{{$store.state.test}}</v-card-title>
          <v-card-actions>
            <v-row>
              <v-col>
                <v-btn block @click="$socket.emit('test')">Test</v-btn>
              </v-col>
              <v-col>
                <v-btn block @click="$store.commit('test', true)">Reset</v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col align-center>
        <p>

        </p>
      </v-col>
    </v-row>
  </v-container>
</template>
