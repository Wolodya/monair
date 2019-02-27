import Vue from 'vue'
import App from './App.vue'
import VueMapbox from 'vue-mapbox';
import Mapbox from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import "vue-swatches/dist/vue-swatches.min.css"


Vue.use(VueMapbox, { mapboxgl: Mapbox });
Vue.use(Vuetify)

new Vue({
    render: h => h(App),
  }).$mount('#app')