import Vue from 'vue/dist/vue.esm';
import { sycn } from 'vuex-router-sync'

import store from '../store'
import router from '../router';

sync(store, router);

document.addEventListener('DOMContentLoader', () => {
   const app = new Vue({
       el: '#app',
       store
   })
});
