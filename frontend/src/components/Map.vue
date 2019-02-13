<template v-if="loaded">
  <div>
    <div id="map">
      <mgl-map :accessToken="accessToken" :mapStyle.sync="mapStyle" 
              :dragRotate="false" :renderWorldCopies="false" :maxBounds="maxBounds"
              :zoom="zoom" :center="center">
          <template v-for="sensor in sensors">
              <mgl-marker :key="sensor.sensor_id" :color="color"
                          :coordinates="[sensor.latitude, sensor.longitude]">
                  <mgl-popup :closeButton="false" class="mobile-charts">
                      <chart :sensor="sensor.sensor_id" :date="date"/>
                  </mgl-popup>
              </mgl-marker>
          </template>
      </mgl-map>
    </div>
  </div>
</template>



<script>
import { MglMap, MglMarker, MglPopup, ImageLayer } from "vue-mapbox";
import Chart from "./Chart.vue";
const axios = require("axios");

export default {
  name: "Map",
  props: ["date"],
  components: {
    MglMap,
    ImageLayer,
    MglMarker,
    MglPopup,
    Chart
  },
  data() {
    return {
      accessToken: "",
      mapStyle: "mapbox://styles/mapbox/streets-v11",
      container:"map",
      color: "#FF3D00",
      maxBounds: [ [-180, -85], [180, 85] ],
      center: [31.1656, 48.3794],
      zoom: 1,
      sensors: [],
      loaded: false
    };
  },
  mounted: function(){
    axios
      .get("/api/sensor-id-location-list/")
      .then(response => {
        this.sensors = response.data;
        this.loaded = true})
  },
}

</script>

<style>
#map{
  position:absolute;
  top:0;
  bottom:0;
  width:100%;
}
.mapboxgl-popup{
  max-width: 330px;
}
</style>