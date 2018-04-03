import 'vuetify/dist/vuetify.min.css';
import 'raivue/dist/raivue.css';

import socketio from 'socket.io-client';
import VueSocketio from 'vue-socket.io';
import Vuetify from 'vuetify';
import Raivue from 'raivue';
import Vue from 'vue';

import App from './App';
import router from './router';
import store from './store';

Vue.config.productionTip = false;

Vue.use(Vuetify);
Vue.use(Raivue);
Vue.use(VueSocketio, `http://${window.location.host}`, store);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
