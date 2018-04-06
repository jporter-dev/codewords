import 'vuetify/dist/vuetify.min.css';
import 'raivue/dist/raivue.css';

import VueSocketio from 'vue-socket.io';
import Vuetify from 'vuetify';
import Raivue from 'raivue';
import Vue from 'vue';

import App from './App';
import router from './router';
import store from './store';
import './registerServiceWorker'

// add bugsnag
import * as bugsnag from 'bugsnag-js'
import * as bugsnagVue from 'bugsnag-vue'
const bugsnagKey = false
if (bugsnagKey) {
  const bugsnagClient = bugsnag(bugsnagKey)
  bugsnagClient.use(bugsnagVue(Vue))
}

Vue.config.productionTip = false;

Vue.use(Vuetify);
Vue.use(Raivue);
Vue.use(VueSocketio, `//${window.location.host}`, store);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
