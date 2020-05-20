import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Try from '@/components/Try'
import piechart from '@/components/piechart'
import statical from '@/components/statical'
import analysis from '@/view/analysis'
import homePage from '@/view/homePage'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'homePage',
      component: homePage
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
      path: '/analysis',
      name: 'analysis',
      component: analysis
    }
  ]
})
