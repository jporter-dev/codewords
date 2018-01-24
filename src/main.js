// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'vuetify/dist/vuetify.min.css';
import 'raivue/dist/raivue.css';

import socketio from 'socket.io-client';
import VueSocketio from 'vue-socket.io';
import Vuetify from 'vuetify';
import Raivue from 'raivue';
import Vue from 'vue';
// import Vuex from 'vuex';
import App from './App';
import router from './router';
import store from './store';

Vue.config.productionTip = false;

Vue.use(Vuetify);
Vue.use(Raivue);
Vue.use(VueSocketio, socketio(`http://${location.host}`), store);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App },
});
