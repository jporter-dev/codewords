import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/views/Home';
import Help from '@/components/views/Help';
import Donate from '@/components/views/Donate';
import Create from '@/components/views/Create';
import Player from '@/components/views/Player';
import Spymaster from '@/components/views/Spymaster';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Root',
      redirect: 'home',
    },
    {
      path: '/home',
      name: 'Home',
      component: Home,
    },
    {
      path: '/create',
      name: 'Create',
      component: Create,
    },
    {
      path: '/help',
      name: 'Help',
      component: Help,
    },
    {
      path: '/donate',
      name: 'Donate',
      component: Donate,
    },
    {
      path: '/:room/player',
      name: 'Player',
      component: Player,
    },
    {
      path: '/:room/spymaster',
      name: 'Spymaster',
      component: Spymaster,
    },
  ],
});
