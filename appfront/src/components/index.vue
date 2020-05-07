<template>
  <div id="index">
    <div class="home">
      <header_com></header_com>
      <el-row type="flex" class="row-bg" justify="center">
        <el-col :span="7">
            <leftGraph></leftGraph>
        </el-col>
        <el-col :span="12">
          <dv-border-box-8></dv-border-box-8>
        </el-col>
        <el-col :span="5">
          <dv-border-box-9>
            <rightGraph></rightGraph>
          </dv-border-box-9>
      </el-row>
    </div>
  </div>
</template>

<script>
import header from '../components/header'
import map from '../components/map'
import piechart from '../components/piechart'
import statical from '../components/statical'
import leftGraph from '../components/leftGraph'
import rightGraph from '../components/rightGraph'

export default {
  data () {
    return {

      pieChartData: [
        { value: 80, name: '云南' },
        { value: 5, name: '北京' },
        { value: 15, name: '山东' },
        { value: 25, name: '河北' },
        { value: 20, name: '江苏' },
        { value: 35, name: '浙江' },
        { value: 30, name: '四川' },
        { value: 40, name: '湖北' }
      ],

      staticalData: [
        ['number', 'amount', 'product'],
        [89.3, 58212, 'Matcha Latte'],
        [57.1, 78254, 'Milk Tea'],
        [74.4, 41032, 'Cheese Cocoa'],
        [50.1, 12755, 'Cheese Brownie'],
        [89.7, 20145, 'Matcha Cocoa'],
        [68.1, 79146, 'Tea']
      ]
    }
  },
  name: 'index',
  components: {
    header_com: header,
    piechart,
    map_com: map,
    statical,
    leftGraph,
    rightGraph
    // piechart_com2: piechart
  },
  methods: {
    // 从后段调取接口更新数据
    getPieData () {
      this.axios.get('http://127.0.0.1:8000/api/get_geodata').then(response => {
        var res = response.data
        console.log(res)
        if (res.error_num === 0) {
          this.pieChartData = res['pieChartData']
        }
      })
    }
  }
}
</script>

<style scoped>
 /* html,body{
      margin:0;
      padding:0;
   } */

.home{
  width: 100%;
  height: 100%;
  background-image: url(http://datav.jiaminghi.com/demo/electronic-file/img/bg.110420cf.png);
  background-repeat: non-repeat;
  background-size: cover;
  padding-bottom: 5%;
}
</style>
