<template>
  <v-navigation-drawer
    temporary
    left
    app
    v-model="drawer"
  >
    <div class="fill-height d-flex flex-column">
      <v-list>
        <v-list-item avatar>
          <v-list-item-avatar>
            <img
              src="@/assets/logo-64x64.png"
              alt="Codenames logo"
            >
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title>Codenames.tv</v-list-item-title>
          </v-list-item-content>
          <v-list-item-action>
            <v-btn
              icon
              @click.stop="drawer = !drawer"
              aria-label="Close drawer"
            >
              <v-icon>mdi-chevron-left</v-icon>
            </v-btn>
          </v-list-item-action>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path"
          :href="item.href"
          router
          link
        >
          <v-list-item-action>
            <v-icon>{{item.icon}}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{item.title}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
      </v-list>
      <v-spacer class="grow"></v-spacer>
      <v-list>
        <v-list-item>
          <v-list-item-subtitle>v{{version}}</v-list-item-subtitle>
        </v-list-item>
      </v-list>
    </div>
  </v-navigation-drawer>
</template>

<script>
import { mapState, mapGetters } from "vuex";

export default {
  data() {
    return {
      menuItems: [
        {
          title: "Home",
          icon: "mdi-home",
          href: "/"
        },
        {
          title: "How to Play",
          icon: "mdi-book-open-variant",
          href: "/help"
        },
        {
          title: "Leave Feedback",
          icon: "mdi-comment-quote",
          href: this.$store.state.feedback_form
        },
        {
          title: "Report a Bug",
          icon: "mdi-bug",
          href: this.$store.state.feedback_form
        },
        {
          title: "Contribute",
          icon: "mdi-xml",
          href: "https://github.com/joshporter1/codenames"
        }
      ]
    };
  },
  computed: {
    ...mapState(["connected", "game"]),
    ...mapGetters(["username"]),
    version() {
      return process.env.VUE_APP_VERSION;
    },
    drawer: {
      get() {
        return this.$store.state.drawer || false;
      },
      set(v) {
        return this.$store.commit("set_drawer", v);
      }
    }
  },
  beforeCreate() {
    this.drawer = false;
  }
};
</script>

<style>
</style>
