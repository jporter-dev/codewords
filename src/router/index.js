import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/views/Home';
import Player from '@/components/views/Player';
import Spymaster from '@/components/views/Spymaster';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/player',
      name: 'Player',
      component: Player,
    },
    {
      path: '/spymaster',
      name: 'Spymaster',
      component: Spymaster,
    },
  ],
});
