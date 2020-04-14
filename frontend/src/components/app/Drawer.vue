<template>
  <v-navigation-drawer
    temporary
    right
    app
    v-model="drawer"
  >
    <v-list class="pa-1">
      <v-list-item
        avatar
        tag="div"
      >
        <v-list-item-action>
          <v-btn
            icon
            @click.stop="drawer = !drawer"
            aria-label="Close drawer"
          >
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>Menu</v-list-item-title>
        </v-list-item-content>
        <v-list-item-avatar>
          <img
            src="@/assets/logo-64x64.png"
            alt="codenames logo"
          />
        </v-list-item-avatar>
      </v-list-item>
    </v-list>
    <v-list
      dense
      two-line
    >
      <v-divider></v-divider>
      <v-list-item>
        <v-list-item-action>
          <v-icon :color="connected ? 'green' : 'red'">mdi-wifi</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>
            Status: {{connected ? 'Connected' : 'Not Connected'}}
          </v-list-item-title>
          <v-list-item-subtitle v-if="connected">
            Connection: {{this.$socket.io.engine.transport.name}}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-divider></v-divider>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState(['connected']),
    drawer: {
      get () { return this.$store.state.drawer },
      set (v) { return this.$store.commit('set_drawer', v) }
    }
  }
}
</script>

<style>

</style>
