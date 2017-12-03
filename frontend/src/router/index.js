import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Greet from '@/components/Greet'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'greet',
      component: Greet
    }
  ]
})
