import Vue from 'vue'
import App from './views/App.vue'
import '../styl/global.styl'
import VueRouter from 'vue-router';
import store from './store'



import index from './views/Index.vue'
import services from './views/Services.vue'



import VueAwesomeSwiper from 'vue-awesome-swiper'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
require('swiper/dist/css/swiper.css')


Vue.use(VueRouter);
Vue.use(VueAwesomeSwiper)


const router = new VueRouter({
  mode: 'history',
  routes:[
    { path: '/', name: 'index' , component: index},
    { path: '/services', name: 'services' , component: services},
  ]
});


new Vue({
  el: '#app',
  components: {
    index,
    services,
    swiper,
    swiperSlide

  },
  router: router,
  store,
  render: h => h(App),

}).$mount('#app');
