<template>
  <v-snackbar
    multi-line
    color="grey lighten-2 black--text"
    light
    :timeout="12300000"
    v-model="showInstallMessage"
    @click.native="hidePopup"
  >
    <img src="@/assets/ios-action.png" alt="codenames logo" id="ios-share">
    To install, click this icon below and then "Add to Homescreen"
    <v-btn flat small class="black--text">
      Close
    </v-btn>

  </v-snackbar>
</template>

<script>
  import { mapState, mapMutations } from 'vuex';

export default {
  name: "ApplePopup",
  data () {
    return {
      showInstallMessage: false,
    }
  },
  computed: {
    ...mapState(['popupHides']),
  },
  methods: {
    ...mapMutations(['incrementPopupHides']),
    hidePopup () {
      this.showInstallMessage = false
      this.incrementPopupHides()
    }
  },
  mounted () {
    const isIos = () => {
      const userAgent = window.navigator.userAgent.toLowerCase();
      return /iphone|ipad|ipod/.test( userAgent );
    }
    // Detects if device is in standalone mode
    const isInStandaloneMode = () => ('standalone' in window.navigator) && (window.navigator.standalone);
    // Checks if should display install popup notification:
    if (this.popupHides <= 2 && isIos() && !isInStandaloneMode()) {
      this.showInstallMessage = true;
    }
  }
}
</script>

<style scoped>
#ios-share {
  width: 32px;
  border-radius: 3px;
  padding: 5px;
  margin-right: 15px;
}
</style>
