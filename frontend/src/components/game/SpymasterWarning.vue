<template>
  <v-container>
    <v-row
      align="center"
      justify="center"
    >
      <v-col
        cols="12"
        sm="8"
        xs="12"
      >
        <v-row>
          <v-col>
            <v-alert
              outlined
              prominent
              text
              type="warning"
              :value="true"
            >
              <b>{{ $t('warning') }}</b> {{ $t('only two spymasters') }}
            </v-alert>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-btn
              block
              large
              color="success"
              @click.prevent="reveal_spymaster"
              id="spymaster-btn"
            >
              {{ $t('make me a spymaster') }}
            </v-btn>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-btn
              block
              large
              color="secondary"
              :to="{name: 'Player', params: {room: $route.params.room } }"
            >
              {{ $t('remain an agent') }}
            </v-btn>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapMutations } from "vuex";
export default {
  methods: {
    ...mapMutations(["reveal_spymaster"])
  }
};
</script>

<style>
</style>

<i18n src="@/plugins/translations/game.json"/>