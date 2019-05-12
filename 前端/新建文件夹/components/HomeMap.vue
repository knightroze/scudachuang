<template>
<main role="main" class="col-lg-10 ml-sm-auto col-md-9 px-4" style="border:gold solid">
<div class="col-lg-12" id="tooltip"></div><!-- div to hold tooltip. -->
<svg class="col-lg-12" id="statesvg"></svg> <!-- svg to hold the map. -->
<button @click="setmapdata()">123</button>
</main>
</template>

<script>
import * as d3 from 'd3'
import {uStates} from '../components/china-zh2.js'
export default {
  name: 'homemap',
  data () {
    return {
      mapdata: {},
      sampleData: [{"city":"BEJ","low":9,"mid":10,"high":8},{"city":"TAJ","low":1,"mid":1,"high":2},{"city":"SHH","low":8,"mid":18,"high":8},{"city":"CHQ","low":2,"mid":4,"high":1},{"city":"HEB","low":0,"mid":0,"high":0},{"city":"SHX","low":1,"mid":0,"high":0},{"city":"LIA","low":0,"mid":0,"high":0},{"city":"JIL","low":0,"mid":1,"high":1},{"city":"HLJ","low":0,"mid":0,"high":0},{"city":"JSU","low":0,"mid":2,"high":0},{"city":"ZHJ","low":2,"mid":2,"high":1},{"city":"ANH","low":0,"mid":1,"high":0},{"city":"FUJ","low":1,"mid":1,"high":2},{"city":"JXI","low":1,"mid":7,"high":1},{"city":"SHD","low":0,"mid":0,"high":1},{"city":"HEN","low":2,"mid":0,"high":1},{"city":"HUB","low":0,"mid":0,"high":0},{"city":"HUN","low":0,"mid":2,"high":0},{"city":"GUD","low":2,"mid":2,"high":2},{"city":"HAI","low":0,"mid":0,"high":1},{"city":"SCH","low":3,"mid":2,"high":2},{"city":"GUI","low":0,"mid":0,"high":0},{"city":"YUN","low":0,"mid":0,"high":0},{"city":"SHA","low":0,"mid":0,"high":0},{"city":"GAN","low":0,"mid":0,"high":0},{"city":"QIH","low":0,"mid":0,"high":0},{"city":"TAI","low":1,"mid":5,"high":3},{"city":"NMG","low":0,"mid":0,"high":0},{"city":"GXI","low":0,"mid":0,"high":0},{"city":"TIB","low":0,"mid":0,"high":0},{"city":"NXA","low":0,"mid":1,"high":0},{"city":"XIN","low":0,"mid":0,"high":0},{"city":"HKG","low":1,"mid":0,"high":0},{"city":"MAC","low":0,"mid":0,"high":1}]
    }
  },
  methods: {
    tooltipHtml: function (n, d) {
      return '<h4>' + n + '</h4><table><tr><td>Low</td><td>' + (d.low) + '</td></tr><tr><td>Mid</td><td>' + (d.mid) + '</td></tr><tr><td>High</td><td>' + (d.high) + '</td></tr></table>'
    },
    setmapdata: function () {
      for (var item in this.sampleData) {
        this.mapdata[item["city"]] = {low:parseInt(item["low"]),high:parseInt(item["high"]), mid:parseInt(item["mid"]), color:d3.interpolate("#ffffcc", "#800026")(parseInt(item["low"]+item["mid"]+item["high"])/100)};
      }
      uStates.draw("#statesvg", this.mapdata, this.tooltipHtml);
    }
  }
}
</script>

<style>
.state{
  fill: none;
  stroke: #a9a9a9;
  stroke-width: 1;
}
.state:hover{
  fill-opacity:0.5;
}
#tooltip {
  text-align: center;
  padding: 20px;
  margin: 10px;
  font: 12px sans-serif;
  background: lightsteelblue;
  border: 1px;
  border-radius: 2px;
  pointer-events: none;
}
#tooltip h4{
  margin:0;
  font-size:14px;
}
#tooltip{
  background:rgba(0,0,0,0.9);
  border:1px solid grey;
  border-radius:5px;
  font-size:12px;
  width:auto;
  padding:4px;
  color:white;
  opacity:0;
}
#tooltip table{
  table-layout:fixed;
}
#tooltip tr td{
  padding:0;
  margin:0;
}
#tooltip tr td:nth-child(1){
  width:50px;
}
#tooltip tr td:nth-child(2){
    text-align:center;
}
</style>
