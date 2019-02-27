

import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import { sync } from 'vuex-router-sync'

Vue.use(BootstrapVue);

import store from '../store'
import router from '../router';

sync(store, router);

import "../../scss/theme/basic"
import HomeApp from './home.vue';

document.addEventListener('DOMContentLoaded', () => {
    const app = new Vue({
        delimiters: ['[[', ']]'],
        el: '#main_app',
        store,
        components: {
            HomeApp
        }
   })
});
