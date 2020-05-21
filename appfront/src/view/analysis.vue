<template>
  <div id="analysis">
    <div class="home">
      <header_com></header_com>
      <el-row>
        <el-button type="primary" @click="getPieData('vic')">VIC</el-button>
        <el-button type="primary" @click="getPieData('nsw')">NSW</el-button>
        <el-button type="primary" @click="getPieData('tas')">Tasmania</el-button>
        <el-button type="primary" @click="getPieData('queens')" >Queensland</el-button>
        <el-button type="primary" @click="getPieData('western')">Western Australia</el-button>
        <el-button type="primary" @click="getPieData('southern')">South Australia</el-button>
      </el-row>
      <el-row type="flex" class="row-bg" justify="center">
        <!-- <el-col :span="2"><el-button type="primary" @click="getPieData" style="float:left; margin: 2px;">新增</el-button></el-col> -->
        <el-col :span="7">
          <leftGraph :election="election" :ageData="ageData"></leftGraph>
        </el-col>
        <el-col :span="11">
          <dv-border-box-8>
            <map_com></map_com>
          </dv-border-box-8>
        </el-col>
        <el-col :span="6">
            <emotionRight :LabelData="LabelData" :LabelData_China="LabelData_China"></emotionRight>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import header from '../part/header'
import map from '../components/map'
import leftGraph from '../part/leftGraph'
import rightGraph from '../part/rightGraph'
import emotionRight from '../part/emotionRight'
import piechart2 from '../components/piechart2'

export default {
  data () {
    return {
      election: [
        { value: 80, name: 'Labour' },
        { value: 5, name: 'Liberal' },
        { value: 25, name: 'National' }
      ],

      ageData: [
        {value: 80, name: '0-10'},
        {value: 200, name: '11-30'},
        {value: 120, name: '31-55'},
        {value: 100, name: 'over 56'}
      ],
      LabelData: [
        {name: 'positive', value: 100},
        {name: 'negative', value: 200}
      ],
      LabelData_China: [
        {name: 'positive', value: 300},
        {name: 'negative', value: 400}
      ]
    }
  },
  name: 'analysis',
  components: {
    header_com: header,
    map_com: map,
    leftGraph,
    emotionRight,
    rightGraph,
    piechart2
    // piechart_com2: piechart
  },
  methods: {
    // 从后段调取接口更新数据
    getPieData (state) {
      console.log('I click!!')
      this.axios.get('http://127.0.0.1:8000/api/get_data?state=' + state).then(response => {
        var res = response.data
        console.log(res)
        if (res.error_num === 0) {
          this.election = res['election']
          this.ageData = res['ageData']
          this.LabelData = res['LabelData']
          this.LabelData_China = res['LsbelData_China']
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

  .home {
    width: 100%;
    height: 100%;
    background-image: url(http://datav.jiaminghi.com/demo/electronic-file/img/bg.110420cf.png);
    background-repeat: non-repeat;
    background-size: cover;
    padding-bottom: 5%;
  }
  .el-button{
    width: 150px;
    margin-bottom: 20px;
    margin-top: 20px;
    margin-left: 50px;
  }
</style>
