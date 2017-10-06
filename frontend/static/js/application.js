import Vue from 'vue'
import App from './views/App.vue'
import '../styl/global.styl'
import VueRouter from 'vue-router';
import store from './store'


Vue.use(VueRouter);


const router = new VueRouter({
  mode: 'history',
  routes:[
  ]
});


new Vue({
  el: '#app',
  components: {
  },
  router: router,
  store,
  render: h => h(App),

}).$mount('#app');
