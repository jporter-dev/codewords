import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/views/Home';
import Create from '@/views/Create';

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
    }, {
      path: '/create',
      name: 'Create',
      component: Create,
    },
    {
      path: '/help',
      name: 'Help',
      component: () => import('@/views/Help'),
    },
    {
      path: '/:room/player',
      name: 'Player',
      component: () => import('@/views/Player'),
    },
    {
      path: '/:room/spymaster',
      name: 'Spymaster',
      component: () => import('@/views/Player'),
      props: {
        spymaster: true
      }
    },
    {
      path: '/test',
      name: 'Test',
      component: () => import('@/views/Test')
    },
  ],
});
