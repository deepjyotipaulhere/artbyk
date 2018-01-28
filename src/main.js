import Vue from 'vue'
import App from './App.vue'
import Header from './Header.vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

import Water from './Water.vue'
import Oil from './Oil.vue'
import Quil from './Quil.vue'
import Ear from './Ear.vue'
import Glass from './Glass.vue'

Vue.use(VueRouter);
Vue.use(VueResource);

const routes=[
  {path:'/water', component:Water},
  {path:'/oil',   component:Oil},
  {path:'/quil',  component:Quil},
  {path:'/glass', component:Glass},
  {path:'/ear',   component:Ear},
];

const router=new VueRouter({
  routes,
  mode:'history'
});

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
