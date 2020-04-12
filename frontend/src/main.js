import 'vuetify/dist/vuetify.min.css';

import Vue from 'vue';
import router from './router';
import store from './store';
import App from './App';
import VueResizeText from 'vue-resize-text';

import vuetify from '@/plugins/vuetify';
import io from "socket.io-client";
import VueSocketIO from "vue-socket.io";

// import './registerServiceWorker'

// add sentry
import * as Sentry from '@sentry/browser';
import * as Integrations from '@sentry/integrations';
if (process.env.VUE_APP_SENTRY_DSN) {
  Sentry.init({
    dsn: process.env.VUE_APP_SENTRY_DSN,
    integrations: [new Integrations.Vue({Vue, attachProps: true})],
  });
}

Vue.config.productionTip = false;
Vue.use(VueResizeText)
Vue.use(new VueSocketIO({
  debug: true,
  connection: io(`http://${window.location.host}`),
  vuex: {
      store,
      actionPrefix: 'WS_',
      mutationPrefix: 'WS_'
  },
}));

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app');
