import Vue from 'vue'
import Router from 'vue-router'
import Error from '@/compoents/Error'
import Greet from '@/components/Greet'
import SharedDir from "@/components/SharedDir"

Vue.use(Router);

export default new Router({
  routes: [
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
      path: '*',
      hidden: true,
      component: Error
    }
  ]
})
