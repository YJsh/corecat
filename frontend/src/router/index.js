import Vue from 'vue'
import Router from 'vue-router'
import Greet from '@/components/Greet'
import Login from '@/components/Login'
import NavMenu from '@/components/NavMenu'
import SharedDir from '@/components/SharedDir'
import Album from '@/components/Album'
import CloudMusic from '@/components/CloudMusic'

Vue.use(Router);

const router =  new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/',
      name: 'greet',
      component: Greet
    },
    {
      path: '/share',
      name: 'share',
      component: SharedDir
    },
    {
      path: '/album',
      name: 'album',
      component: Album
    },
    {
      path: '/nav',
      name: 'navMenu',
      component: NavMenu,
    },
    {
      path: '/cloudMusic',
      name: 'cloudMusic',
      component: CloudMusic,
    }
  ]
});

router.beforeEach((to, from, next) => {
  if ("/login" !== to.path && (!router.app.$cookie || !router.app.$cookie.get("token"))) {
    router.push("/login");
    return;
  }
  next();
});

export default router;
