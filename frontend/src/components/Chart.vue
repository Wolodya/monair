<template v-if="loaded">
  <v-expansion-panel class="expansion scroll-bar" >
    <v-expansion-panel-content v-for="(value, attr) in sensor_data" :key="attr + sensor">
      <div slot="header" class="header">{{attr.toUpperCase()}}</div>
        <div :id="attr + sensor" class="card"></div>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>


<script>
import { MglPopup}  from "vue-mapbox";
import Plotly from "plotly.js-dist";
import _ from "underscore";
const axios = require("axios");

export default {
    name: "Chart",
    props: {
        sensor: Number, 
        date: String
    },
    watch: {
        date: function(newVal, oldVal){
            this.get_data_24h()
        }
    },
    data(){
        return{
            sensor_data: {},
            loaded: false,
        }
    },
    methods:{
        get_data_24h(){
            var self=this;
            axios
                .get("/api/sensor-data-24h/" + self.sensor + "/" + "?date=" + self.date)
                .then(response => {
                    self.sensor_data = response.data["24h"];
                })
                .finally(() => {
                    self.loaded = true;
                    self.render_charts()
                })
        },
        render_charts(){
            var layout = {
                    width: 320,
                    height: 120,
                    margin: { l: 35, r: 25, b: 20, t: 25, p: 4 },
                    xaxis: {
                        showticklabels: false
                    }
                };            
            for (var attr in this.sensor_data){
                var data = [{
                    x: _.range(1, 25),
                    y: Object.values(this.sensor_data[attr]),
                    text: Object.keys(this.sensor_data[attr]),
                    type: "bar",
                    marker: {
                        color: "#0277BD"
                    }
                }];
                try{
                    Plotly.react(attr + this.sensor, data, layout, {displayModeBar: false});
                }
                catch(e){ }
            }
        } 
    },
    mounted: function(){
        this.get_data_24h();
    },
}
</script>

<style lang="sass">
$scroll-back:  #F5F5F5;
.expansion{
    max-height: 400px;
	overflow-y: scroll;
    overflow-x: hidden;
}
.card{
    margin: 0 auto,
};
.scroll-bar::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
	background-color: $scroll-back;
}
.scroll-bar::-webkit-scrollbar
{
	width: 6px;
	background-color: $scroll-back;
}
.scroll-bar::-webkit-scrollbar-thumb
{
	background-color: #757575;
}
.fixeddiv{
    position: fixed;
    bottom: 0;
}
</style>
