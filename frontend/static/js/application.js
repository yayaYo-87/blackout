//js
import Vue from 'vue'
import App from './views/App.vue'
import '../styl/global.styl'
import VueRouter from 'vue-router';
import VueYouTubeEmbed from 'vue-youtube-embed'
import '../styl/scrollbar.css'
import store from './store'
var VueScrollTo = require('vue-scrollto');

//Страницы
import index from './views/Index.vue';
import services from './views/Services.vue';
import servicesItem from './views/ServicesItem.vue';
import catalog from './views/Catalog.vue';
import catalogCategory from './views/CatalogCategory.vue';
import catalogItem from './views/CatalogItem.vue';
import project from './views/Project.vue';
import projectCategory from './views/ProjectCategory.vue';
import projectItem from './views/ProjectItem.vue';
import partners from './views/Partners.vue';
import about from './views/About.vue';
import contacts from './views/Contacts.vue';

//Плагины
import VueAwesomeSwiper from 'vue-awesome-swiper'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
require('swiper/dist/css/swiper.css')


Vue.use(VueRouter);
Vue.use(VueAwesomeSwiper);
Vue.use(VueYouTubeEmbed);
Vue.use(VueScrollTo, {
     container: "body",
     duration: 500,
     easing: "ease",
     offset: -80,
     cancelable: true,
     onDone: false,
     onCancel: false,
     x: false,
     y: true
 })

//При переходе скролит до верха
const scrollBehavior = (to, from, savedPosition) => {
  if (to.hash) {
    console.log(to.hash)
    return {
      selector: to.hash,
    }
  } else {
    return { x: 0, y: 0 }
  }
};

const router = new VueRouter({
  mode: 'history',
  scrollBehavior,
  routes:[
    { path: '/', name: 'index' , component: index},
    { path: '/service', name: 'services' , component: services},
    { path: '/service/:id', name: 'servicesItem' , component: servicesItem},
    { path: '/catalog', name: 'catalog' , component: catalog},
    { path: '/catalog/:id', name: 'catalogCategory' , component: catalogCategory},
    { path: '/catalog/:id/:item', name: 'catalogItem' , component: catalogItem},
    { path: '/project', name: 'project' , component: project},
    { path: '/project/:id', name: 'projectCategory' , component: projectCategory},
    { path: '/project/:id/:item', name: 'projectItem' , component: projectItem},
    // { path: '/partners', name: 'partners' , component: partners},
    { path: '/about', name: 'about' , component: about},
    { path: '/contacts', name: 'contacts' , component: contacts},
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
    catalogItem,
    partners,
    about,
    contacts
  },
  router: router,
  store,
  render: h => h(App),

}).$mount('#app');
