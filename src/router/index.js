import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/views/Home';
import Help from '@/views/Help';
import Create from '@/views/Create';
import Player from '@/views/Player';
import Spymaster from '@/views/Spymaster';

Vue.use(Router);

export default new Router({
  mode: 'history',
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
