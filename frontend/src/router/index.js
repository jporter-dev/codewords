import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/views/Home';
import Create from '@/views/Create';
const Player = () => import('@/views/Player')
const Help = () => import('@/views/Help')

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [{
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/home',
      redirect: '/',
    },
    {
      path: '/help',
      name: 'Help',
      component: Help,
    },
    {
      path: '/create',
      name: 'Create',
      component: Create,
    },
    {
      path: '/:room/player',
      name: 'Player',
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
