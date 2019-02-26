import '../../scss/_base.scss';
import Vue from 'vue/dist/vue.esm.js';
import { sync } from 'vuex-router-sync'

import store from '../store'
import router from '../router';

sync(store, router);

import HomeApp from './home.vue';

document.addEventListener('DOMContentLoaded', () => {
   const app = new Vue({
       el: '#main_app',
       store,
       components: {
           HomeApp
       }
   })
});
