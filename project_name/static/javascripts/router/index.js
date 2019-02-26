import Vue from 'vue/dist/vue.esm';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    mode: 'history',
    scrollBehavior: () => ({y: 0}),
    routes: []
});
