//js
import Vue from 'vue'
import App from './views/App.vue'
import '../styl/global.styl'
import VueRouter from 'vue-router';
import store from './store'

//Страницы
import index from './views/Index.vue'
import services from './views/Services.vue'
import servicesItem from './views/ServicesItem.vue'
import catalog from './views/Catalog.vue'
import catalogCategory from './views/CatalogCategory.vue'
import catalogItem from './views/CatalogItem.vue'
import project from './views/Project.vue'

//Плагины
import VueAwesomeSwiper from 'vue-awesome-swiper'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
require('swiper/dist/css/swiper.css')


Vue.use(VueRouter);
Vue.use(VueAwesomeSwiper)


//При переходе скролит до верха
const scrollBehavior = (to, from, savedPosition) => {
    return { x: 0, y: 0 }
};

const router = new VueRouter({
  mode: 'history',
  scrollBehavior,
  routes:[
    { path: '/', name: 'index' , component: index},
    { path: '/services', name: 'services' , component: services},
    { path: '/services/:id', name: 'servicesItem' , component: servicesItem},
    { path: '/catalog', name: 'catalog' , component: catalog},
    { path: '/catalog/сategory', name: 'catalogCategory' , component: catalogCategory},
    { path: '/catalog/сategory/catalogItem', name: 'catalogItem' , component: catalogItem},
    { path: '/project', name: 'project' , component: project},
  ]
});


new Vue({
  el: '#app',
  components: {
    index,
    services,
    servicesItem,
    catalog,
    catalogCategory,
    project,
    swiper,
    swiperSlide,
    catalogItem

  },
  router: router,
  store,
  render: h => h(App),

}).$mount('#app');
