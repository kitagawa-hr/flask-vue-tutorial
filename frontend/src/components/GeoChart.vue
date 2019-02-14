<template>
  <div id="contents">
    <button @click="getPopulationData">Reflesh</button>
    <h5>{{popData}}</h5>
    <GChart :settings="chartSettings" type="GeoChart" :data="chartData" :options="chartOptions"/>
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'
import axios from 'axios'

export default {
  components: {
    GChart
  },
  data () {
    return {
      chartSettings: {
        packages: ['geochart'],
        mapsApiKey: 'AIzaSyAUhU0YFPXmxmelHkDilps0l5p6FKAr_GQ'
      },
      chartData: Array(this.getPopulationData()),
      chartOptions: {
        region: 'JP',
        resolution: 'provinces',
        backgroundColor: '#ebf7fe',
        colors: ['white', 'red'],
        displayMode: 'regions'
      }
    }
  },
  methods: {
    getPopulationData () {
      var array = [['Pref', 'Population']].concat(this.getDataFromBackEnd())
      this.popData = array
      return array
    },
    getDataFromBackEnd () {
      const path = `http://localhost:5000/api/population/all`
      axios
        .get(path)
        .then(response => {
          this.popData = response.data.population
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
