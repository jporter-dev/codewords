import 'vuetify/dist/vuetify.min.css';

import Vue from 'vue';
import router from './router';
import store from './store';

import App from './App';
import VueResizeText from 'vue-resize-text';

import vuetify from '@/plugins/vuetify';
import io from "socket.io-client";
import VueSocketIO from "vue-socket.io";
import IdleVue from 'idle-vue'
// import './registerServiceWorker'
// navigator.serviceWorker.getRegistrations().then(function(registrations) {
//   for(let registration of registrations) {
//     registration.unregister()
//   }
// })

// add sentry
import * as Sentry from '@sentry/browser';
import * as Integrations from '@sentry/integrations';
if (process.env.VUE_APP_SENTRY_DSN) {
  Sentry.init({
    dsn: process.env.VUE_APP_SENTRY_DSN,
    integrations: [new Integrations.Vue({
      Vue,
      attachProps: true
    })],
  });
}

Vue.config.productionTip = false;
Vue.use(VueResizeText)
Vue.use(new VueSocketIO({
  debug: false,
  connection: io(`//${window.location.host}`),
  vuex: {
    store,
    actionPrefix: 'WS_',
    mutationPrefix: 'WS_'
  },
}));
// IdleVue to disconnect after 1h idle time
Vue.use(IdleVue, {
  store,
  idleTime: 3600000 // 60 minutes
});

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app');
