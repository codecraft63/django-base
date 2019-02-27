import "../../scss/theme/basic"

import Vue from 'vue';
import { sync } from 'vuex-router-sync'

import store from '../store'
import router from '../router';

sync(store, router);

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
