<template>
  <v-container fill-height>
    <v-row justify="center">
      <v-col
        cols="12"
        sm="8"
        md="8"
        lg="6"
        xl="6"
        justify="center"
      >
        <v-row justify="center">
          <v-avatar
            tile
            size="128"
          >
            <img
              src="@/assets/logo-256x256.png"
              alt="codenames logo"
            >
          </v-avatar>
        </v-row>
        <v-row
          align="center"
          justify="center"
        >
          <h2 class="cn-text">{{ $t('title') }}</h2>
        </v-row>
        <v-row>
          <v-col>
            <v-card>
              <v-card-text class="body-1">
                <p>
                  Time for some unfortunate yet expected news...
                  Czech Games Edition, the creators of Codenames, have
                  have kindly reached out to me requesting that I take down this
                  unofficial version of their game. The official
                  version is playable at the link below.
                </p>
                <p>
                  I originally built this site as an educational programming
                  project, and it has fully served that purpose and then some.
                  I never imagined it gaining the popularity and traffic that it
                  did, and I would like to thank every one of you for the support.
                  Although the site has been taken down, the original source code
                  will remain available on GitHub.
                </p>
                <v-btn
                  v-for="(link,title) in links"
                  :key="link"
                  :href="link"
                  class="mt-2"
                  block
                >
                  {{title}}
                </v-btn>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      links: {
        "Follow Me": "https://twitter.com/codecaffeinated",
        "Contact Me": "mailto:codecaffeinated@gmail.com",
        "Blog Series":
          "https://medium.com/hackervalleystudio/weekend-project-part-1-creating-a-real-time-web-based-application-using-flask-vue-and-socket-b71c73f37df7",
        "View Source": "https://github.com/joshporter1/codenames",
        "Buy Me a Coffee": "https://www.buymeacoffee.com/codecaffeinated",
        "Buy Codenames":
          "https://amzn.to/2P6Aklv",
        "Play Codenames": "https://codenames.game"
      }
    };
  }
};
</script>

<i18n src="@/plugins/translations/takedown.json"/>
