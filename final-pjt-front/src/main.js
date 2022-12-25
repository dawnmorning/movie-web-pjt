import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
Vue.use(IconsPlugin)
Vue.use(BootstrapVue)
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueNumber from 'vue-number-animation'

Vue.use(VueNumber)


import 'animate.css';


/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUserSecret)

/* add font awesome icon component */
Vue.component('font-awesome-icon', FontAwesomeIcon)


import VueGlide from 'vue-glide-js'
Vue.use(VueGlide)


Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
