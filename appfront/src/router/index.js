import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import Try from '@/components/Try'
import index from '@/components/index'
import piechart from '@/components/piechart'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },

    {
      path: '/Home',
      name: 'Home',
      component: Home
    },

    {
      path: '/Try',
      name: 'Try',
      component: Try
    },

    {
      path: '/index',
      name: 'index',
      component: index
    },

    {
      path: '/pie',
      name: 'piechart',
      component: piechart
    }
  ]
})
