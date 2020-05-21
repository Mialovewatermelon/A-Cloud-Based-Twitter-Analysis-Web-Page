<template>
  <div class="container-item">
    <div class="box-item">
      <dv-border-box-1>
        <dv-decoration-11 style="width:200px;height:60px;" class="title">PIE CHART</dv-decoration-11>
        <piechart :election="election"></piechart>
      </dv-border-box-1>
    </div>
    <div class="box-item">
      <dv-border-box-1>
        <dv-decoration-11 style="width:250px;height:60px;" class="title">STATICAL RATING</dv-decoration-11>
        <piechart2 :ageData="ageData"></piechart2>
      </dv-border-box-1>
    </div>
  </div>
</template>

<script>
import piechart from '../components/piechart'
import piechart2 from '../components/piechart2'
export default {
  props: {
    election: {
      type: Array
    },
    ageData: {
      type: Array
    }
  },

  data () {
    return {
    }
  },
  name: 'left',
  components: {
    piechart,
    piechart2
  }
}
</script>
<style>
  .title {
    font-weight: 700;
    font-size: 20px;
    width: 200px;
    height: 60px;
    display: block;
    margin: 0 auto;
    color: white
  }
</style>
