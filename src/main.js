import Vue from 'vue'
import App from './App.vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import Vuelidate from 'vuelidate'

Vue.config.productionTip = false
Vue.use(Buefy, {defaultIconPack: 'fas'})
Vue.use(Vuelidate)

new Vue({
  render: h => h(App),
}).$mount('#app')
