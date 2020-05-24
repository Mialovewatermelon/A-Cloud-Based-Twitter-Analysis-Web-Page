<template>
  <div id="analysis">
    <div class="home">
      <header_com></header_com>
      <el-row>
        <el-button type="primary" @click="getPieData('vic', 'Victoria')">Victoria</el-button>
        <el-button type="primary" @click="getPieData('nsw', 'New South Wales')">New South Wales</el-button>
        <el-button type="primary" @click="getPieData('tas', 'Tasmania')">Tasmania</el-button>
        <el-button type="primary" @click="getPieData('queens', 'Queensland')" >Queensland</el-button>
        <el-button type="primary" @click="getPieData('western', 'Western Australia')">Western Australia</el-button>
        <el-button type="primary" @click="getPieData('southern', 'South Australia')">South Australia</el-button>
      </el-row>
      <el-row type="flex" class="row-bg" justify="center">
        <!-- <el-col :span="2"><el-button type="primary" @click="getPieData" style="float:left; margin: 2px;">新增</el-button></el-col> -->
        <el-col :span="7">
          <leftGraph :election="election" :ageData="ageData" :state="state"></leftGraph>
        </el-col>
        <el-col :span="11">
          <dv-border-box-8>
            <map_com></map_com>
          </dv-border-box-8>
        </el-col>
        <el-col :span="6">
            <emotionRight :LabelData="LabelData" :LabelData_China="LabelData_China" :state="state"></emotionRight>
        </el-col>
      </el-row>
      <el-row>
        <dv-border-box-10 style="width:100%; height:120%; margin-bottom:50px">
        <textBelow :TextData_pos="TextData_pos" :TextData_neg="TextData_neg" :TextData_china_pos="TextData_china_pos" :TextData_china_neg="TextData_china_neg" style="margin-bottom:30px"></textBelow>
        </dv-border-box-10>
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
import textBelow from '../part/textBelow'
export default {
  data () {
    return {
      election: [
        {name: 'labor party', value: 165394},
        {name: 'national coalition', value: 129032}
      ],

      ageData: [
        {name: '0~14 years old', value: 0.1788},
        {name: '15~64 years old', value: 0.6284},
        {name: '65+ years old', value: 0.1928}
      ],
      LabelData: [
        {name: 'positive', value: 12348},
        {name: 'negative', value: 5947}
      ],
      LabelData_China: [
        {name: 'positive', value: 8},
        {name: 'negative', value: 8}
      ],
      state: 'Victoria',
      TextData_pos: [ ],
      TextData_neg: [],
      TextData_china_pos: [],
      TextData_china_neg: []

    }
  },
  mounted () {
    this.getPieData('vic', 'Victoria')
  },
  name: 'analysis',
  components: {
    header_com: header,
    map_com: map,
    leftGraph,
    emotionRight,
    rightGraph,
    textBelow
    // piechart_com2: piechart
  },
  methods: {
    // 从后段调取接口更新数据
    getPieData (state, stateName) {
      console.log('I click!!')
      this.axios.get('http://127.0.0.1:8000/api/get_data?state=' + state).then(response => {
        console.log(window.location.host)
        var res = response.data
        this.state = stateName
        console.log(res)
        if (res.msg === 0) {
          this.election = res['election']
          console.log('>>>>' + this.election)
          this.ageData = res['ageData']
          console.log('>>>>' + this.ageData)
          this.LabelData = res['LabelData']
          this.LabelData_China = res['LabelData_China']
          this.TextData_pos = res['TextData_pos']
          this.TextData_neg = res['TextData_neg']
          this.TextData_china_pos = res['TextData_china_pos']
          this.TextData_china_neg = res['TextData_china_neg']
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
