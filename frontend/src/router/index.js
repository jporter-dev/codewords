import Vue from 'vue';
import Router from 'vue-router';
import Takedown from '@/views/Takedown';
import Create from '@/views/Create';
const Home = () => import('@/views/Home')
const Player = () => import('@/views/Player')
const Help = () => import('@/views/Help')

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [{
      path: '/',
      name: 'Takedown',
      component: Takedown,
    },
    {
      path: '/home',
      name: 'Home',
      alias: ['/play', '/game'],
      component: Home,
    },
    {
      path: '/help',
      name: 'Help',
      component: Help,
    }, {
      path: '/create',
      name: 'Create',
      component: Create,
    },
    {
      path: '/:room',
      name: 'Player',
      component: Player,
    },
    {
      path: '/:room/player',
      name: 'PlayerView',
      component: Player,
    },
    {
      path: '/:room/spymaster',
      name: 'Spymaster',
      component: Player,
      props: {
        spymaster: true
      }
    },
  ],
});
