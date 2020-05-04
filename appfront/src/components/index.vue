<template>
  <div id="index">
    <header_com></header_com>
    <div class="'content">
      <el-row>
        <el-button type="primary" @click="getPieData" style="float:left; margin: 2px;">新增</el-button>
      </el-row>
      <el-row>
        <piechart_com :pieChartData="pieChartData"></piechart_com>
      </el-row>
    </div>
  </div>
</template>

<script>
import header from '../components/header'
import map from '../components/map'
import piechart from '../components/piechart'

export default {
  data () {
    return {
      pieChartData: [{value: 0, name: null}]
    }
  },
  name: 'index',
  components: {
    header_com: header,
    piechart_com: piechart,
    map_com: map
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
</style>
