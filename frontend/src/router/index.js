import Vue from 'vue'
import Router from 'vue-router'
// import Error from '@/compoents/Error'
import Greet from '@/components/Greet'
import Login from '@/components/Login'
import NavMenu from '@/components/NavMenu'
import SharedDir from '@/components/SharedDir'
import Album from '@/components/Album'

Vue.use(Router);

export default new Router({
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
    }
    // {
    //   path: '*',
    //   hidden: true,
    //   component: Error
    // }
  ]
})
