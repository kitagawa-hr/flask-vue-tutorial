import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import About from '@/components/About'
import Chart from '@/components/Chart'
import GeoChart from '@/components/GeoChart'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [{
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/chart',
    name: 'Chart',
    component: Chart
  },
  {
    path: '/geochart',
    name: 'GeoChart',
    component: GeoChart
  }
  ]
})
