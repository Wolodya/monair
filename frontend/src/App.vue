<template>
  <v-app :style="cssProps">
    <v-toolbar :color="maincolor" app>
      <v-toolbar-title class="pa-4" id="title">Monair</v-toolbar-title>
      <v-spacer></v-spacer>
      <swatches v-model="maincolor" :colors="colors" row-length="3"
                shapes="circles" show-border popover-to="left">
        <v-btn slot="trigger" :color="'#424242'" fab small dark>
          <v-icon>color_lens</v-icon>
        </v-btn>
      </swatches>
    </v-toolbar>
    <v-content>
      <Map :date="date"></Map> 
      <template v-if='mobile'>
        <v-dialog ref="dialog" v-model="modal" id="datepiker"
                  :return-value.sync="date" persistent lazy full-width width="290px">
          <v-btn fab dark slot="activator" :color='maincolor' v-model="date">
            <v-icon>date_range</v-icon>
          </v-btn>
          <v-date-picker v-model="date" :color="maincolor">
            <v-spacer></v-spacer>
            <v-btn flat color="primary" @click="modal = false">Cancel</v-btn>
            <v-btn flat color="primary" @click="$refs.dialog.save(date)">OK</v-btn>
          </v-date-picker>
        </v-dialog>
      </template>
      <template v-else>
        <v-date-picker id="datepiker" :color="maincolor" v-model="date"></v-date-picker>
      </template>
    </v-content>
  </v-app>
</template>

<script>
import Map from "./components/Map.vue";
import Swatches from 'vue-swatches'

export default {
  name: "App",
  components: {
    Map,
    Swatches
  },
  data(){
    return{
      date: new Date().toISOString().substr(0, 10),
      maincolor: 'rgb(174, 234, 0)',
      colors:  ['#AEEA00', '#FF8F00', '#558B2F', '#00838F', '#009688', '#607D8B', ],
      modal: false
    }
  },
  computed: {
    cssProps() { return {
        '--maincolor': this.maincolor
      }
    },
    mobile(){
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return true
        case 'sm': return true
        case 'md': return false
        case 'lg': return false
        case 'xl': return false
      }
    }
	}
}
</script>

<style lang="sass">
@import url("https://fonts.googleapis.com/css?family=IBM+Plex+Mono");
$main-color: var(--maincolor);

html, body{
overflow-y:hidden !important;
overflow-x:hidden !important;
}
#title{
  font-family: "IBM Plex Mono", monospace;
  font-style: italic;
  font-size: x-large;
}
#datepiker{
  position: fixed;
  right: 0;
  bottom: 1%;
}
.v-expansion-panel__header{
    min-height: 1px;
}
.v-expansion-panel__container--active > .v-expansion-panel__header{
    background-color: $main-color !important;;
}
.mapboxgl-popup-anchor-top-left .mapboxgl-popup-tip,
.mapboxgl-popup-anchor-top-right .mapboxgl-popup-tip,
.mapboxgl-popup-anchor-top .mapboxgl-popup-tip
{
    border-bottom-color: $main-color !important;;
}
.mapboxgl-popup-anchor-bottom-left .mapboxgl-popup-tip,
.mapboxgl-popup-anchor-bottom-right .mapboxgl-popup-tip,
.mapboxgl-popup-anchor-bottom .mapboxgl-popup-tip
{
    border-top-color: $main-color !important;;
}
.mapboxgl-popup-content{
    background-color: $main-color !important;
    padding: 8px;
}
</style>
