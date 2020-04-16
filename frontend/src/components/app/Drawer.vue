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
      class="pt-0"
      dense
    >
      <v-divider></v-divider>
      <v-list-item
        v-for="item in menuItems"
        :key="item.title"
        router
        :to="item.path"
        :href="item.href"
      >
        <v-list-item-action>
          <v-icon>{{item.icon}}</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>{{item.title}}</v-list-item-title>
        </v-list-item-content>
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
    <v-list v-if="game.players">
      <v-list-item>
        <v-list-item-subtitle>Current Players</v-list-item-subtitle>
        <v-list-item-avatar>
          <v-chip small>{{Object.keys(game.players.players).length}}</v-chip>
        </v-list-item-avatar>
      </v-list-item>
      <v-list-item
        v-for="(name,id) in game.players.players"
        :key="id"
        :title="id"
      >
        <v-list-item-icon>
          <v-icon v-if="game.players.spymasters.indexOf(id) >= 0" color="primary">mdi-library</v-icon>
          <v-icon v-else>mdi-account</v-icon>
        </v-list-item-icon>
        <v-list-item-title>{{name}}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      menuItems: [
        {
          title: "Leave Feedback",
          icon: "mdi-comment-quote",
          href:
            "https://docs.google.com/forms/d/e/1FAIpQLSfLs3pnKu7WifF4WQdq0Q8VAtiY1WARyw8O_rmrxjYnm7Zz1g/viewform?usp=sf_link"
        },
        {
          title: "Report a Bug",
          icon: "mdi-bug",
          href:
            "https://docs.google.com/forms/d/e/1FAIpQLSfLs3pnKu7WifF4WQdq0Q8VAtiY1WARyw8O_rmrxjYnm7Zz1g/viewform?usp=sf_link"
        },
        {
          title: "Contribute",
          icon: "mdi-xml",
          href: "https://github.com/joshporter1/codenames"
        },
        {
          title: "Contact",
          icon: "mdi-email",
          href:
            "https://docs.google.com/forms/d/e/1FAIpQLSfLs3pnKu7WifF4WQdq0Q8VAtiY1WARyw8O_rmrxjYnm7Zz1g/viewform?usp=sf_link"
        }
      ]
    };
  },
  computed: {
    ...mapState(["connected", "game"]),
    drawer: {
      get() {
        return this.$store.state.drawer;
      },
      set(v) {
        return this.$store.commit("set_drawer", v);
      }
    }
  }
};
</script>

<style>
</style>
