import Vue from 'vue'
import VueCookie from 'vue-cookie'
import axios from 'axios'
import VueAxios from 'vue-axios'
import sidebar from './components_dash/sidebar.vue'
import doc_placeholders from './components_dash/doc_placeholders.vue'
import dash from'./components_dash/dash.vue'
import lodash from 'lodash'

Vue.use(VueAxios, axios)
Vue.use(lodash)
Vue.use(VueCookie)

window.Event = new Vue();

new Vue(sidebar).$mount(".sidebar");
new Vue(doc_placeholders).$mount(".doc_placeholders");
new Vue(dash).$mount(".dash");
