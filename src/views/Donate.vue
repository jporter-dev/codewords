<template>
  <v-layout align-start justify-center row fill-height>
    <v-flex md6>
      <v-card flat>
        <v-card-text px-0 class='text-xs-center'>
          <center>
            <h4><v-icon medium>favorite</v-icon> Support Us!</h4>
            <p>
              If you enjoy the app, feel free to donate to help support future updates<br/>
              and to keep the servers running, or just to buy me a beer! <span class="title">🍻</span>
            </p>
            <v-flex sm5 xs11>
              <v-btn block large color="primary" href="https://www.paypal.me/joshporter1">PayPal</v-btn>
            </v-flex>
            <NanoPayment
              address="xrb_3ui4sg4jjdxsfwshjcbkjnthdzmtbgxe7pa597cxsa4aamkkj3b8dmeome4i"
              :amount="2500000"
            ></NanoPayment>
          </center>
          <div>Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
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
