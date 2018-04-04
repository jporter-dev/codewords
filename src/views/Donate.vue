<template>
  <v-layout row wrap pt-5>
    <v-flex>
      <v-card flat>
        <v-card-text px-0 class='text-xs-center'>
          <center>
            <h4><v-icon medium>favorite</v-icon> Support Us!</h4>
            <p>
              If you enjoy the app, feel free to donate to help support future updates<br/>
              and to keep the servers running, or just to buy me a beer! <span class="title">🍻</span>
            </p>
            <v-flex sm2 xs12>
              <v-btn block round large color="primary" href="https://www.paypal.me/joshporter1">PayPal</v-btn>
            </v-flex>
            <RaiDonation
              address="xrb_3ui4sg4jjdxsfwshjcbkjnthdzmtbgxe7pa597cxsa4aamkkj3b8dmeome4i"
              label="Donate"
            ></RaiDonation>
          </center>
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: 'donate',
};
</script>
