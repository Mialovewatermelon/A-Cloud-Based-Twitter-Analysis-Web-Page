<template>
    <div class="container mt-4">
        <h2 class="text-center text-secondary pb-2">Australia Map</h2>
        <div class="map-container border rounded">
            <ul class="nav justify-content-center border-bottom">
                <!--營運地區 nav-->
            </ul>
            <!--地圖呈現在此-->
            <div class="google-map" id="map"></div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Restaurants',
  data () {
    return {
      mapAddress: 'https://data.gov.au/geoserver/vic-local-government-areas-psma-administrative-boundaries/wfs?request=GetFeature&typeName=ckan_bdf92691_c6fe_42b9_a0e2_a4cd716fa811&outputFormat=json',
      // 預設經緯度在信義區附近
      lat: 25.0325917,
      lng: 121.5624999
    }
  },
  mounted () {
    this.initMap()
    // this.setMarker();
  },
  methods: {

    // 建立地圖
    initMap () {
      let myChart = this.$echarts.init(document.getElementById('map'), 'temp')
      myChart.showLoading()

      // eslint-disable-next-line no-undef
      this.$axios.get(this.mapAddress).then((response) => {
        myChart.hideLoading()
        console.log(response)
        this.$echarts.registerMap('VIC', response)
        console.log(this.$echarts.getMap('VIC').geoJson)
        let option = {
          title: {
            text: 'USA Population Estimates (2012)',
            subtext: 'Data from www.census.gov',
            sublink: 'http://www.census.gov/popest/data/datasets.html',
            left: 'right'
          },
          tooltip: {
            trigger: 'item',
            showDelay: 0,
            transitionDuration: 0.2,
            formatter: function (params) {
              var value = (params.value + '').split('.')
              value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,')
              return params.seriesName + '<br/>' + params.name + ': ' + value
            }
          },
          visualMap: {
            left: 'right',
            min: 500000,
            max: 38000000,
            inRange: {
              color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
            },
            text: ['High', 'Low'], // 文本，默认为数值文本
            calculable: true
          },
          toolbox: {
            show: true,
            // orient: 'vertical',
            left: 'left',
            top: 'top',
            feature: {
              dataView: {readOnly: false},
              restore: {},
              saveAsImage: {}
            }
          },
          series: [
            {
              name: 'VIC PopEstimates',
              type: 'map',
              roam: true,
              map: 'VIC',
              nameProperty: 'vic_lga__3',
              emphasis: {
                label: {
                  show: true
                }
              },
              // 文本位置修正
              textFixed: {
                Alaska: [20, -20]
              },
              data: [
                {name: 'MELBOURNE', value: 4822023}
                // {id:"ckan_bdf92691_c6fe_42b9_a0e2_a4cd716fa811.83", value: 12324212}
              ]
            }
          ]
        }
        myChart.setOption(option)
        // myChart.properties.name = myChart.properties.vic_lga__3
      })
    },
    // 建立地標
    setMarker () {
      // 建立一個新地標
      // const marker = new google.maps.Marker({
      //     // 設定地標的座標
      //     position: { lat: this.lat, lng: this.lng },
      //     // 設定地標要放在哪一個地圖
      //     map: this.map
      // });
    }
  }
}
</script>

<style scoped>
    .google-map{
        width : 500px;
        height : 300px;
    }
</style>
