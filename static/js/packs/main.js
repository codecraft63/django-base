import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import {sync} from 'vuex-router-sync'
import store from '../store'
import router from '../router';
import "~/theme/basic.scss";
Vue.use(BootstrapVue);

sync(store, router);

document.addEventListener('DOMContentLoaded', () => {

  const AppHome = () => import('@/components/Core/Home');

  const app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    store,
    components: {
      AppHome
    }
  })
});
