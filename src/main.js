// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'vuetify/dist/vuetify.min.css';

import socketio from 'socket.io-client';
import VueSocketio from 'vue-socket.io';
import Vuetify from 'vuetify';
import Vue from 'vue';
// import Vuex from 'vuex';
import App from './App';
import router from './router';

Vue.config.productionTip = false;

Vue.use(Vuetify);
Vue.use(VueSocketio, socketio('http://jporter-dev:5000'));

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App },
  sockets: {
    connect() {
      console.log('connected');
    },
    message(msg) {
      console.log(JSON.stringify(msg));
    },
  },
});
