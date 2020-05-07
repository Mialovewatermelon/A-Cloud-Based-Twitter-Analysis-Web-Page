import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import Try from '@/components/Try'
import index from '@/components/index'
import piechart from '@/components/piechart'
import statical from '@/components/statical'
import leftGraph from '@/components/leftGraph'
import header from '@/components/header'
import rightGraph from '@/components/rightGraph'
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
    },

    {
      path: '/statical',
      name: 'statical',
      component: statical
    },
    {
      path: '/left',
      name: 'leftGrapht',
      component: leftGraph
    },
    {
      path: '/header',
      name: 'header',
      component: header
    },
    {
      path: '/right',
      name: 'rightGraph',
      component: rightGraph
    }
  ]
})
