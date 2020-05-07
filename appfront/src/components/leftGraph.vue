<template>
    <div class="container-item">
        <div class="box-item">
            <dv-border-box-1>
                <dv-decoration-11 style="width:200px;height:60px;" class="title">PIE CHART</dv-decoration-11>
                <piechart :pieChartData="pieChartData"></piechart>
            </dv-border-box-1>
        </div>
        <div clas="box-item">
            <dv-border-box-1>
                <dv-decoration-11 style="width:250px;height:60px;" class="title">STATICAL RATING</dv-decoration-11>
              <statical :staticalData="staticalData"></statical>
            </dv-border-box-1>
        </div>
    </div>
</template>

<script>
import piechart from '../components/piechart'
import statical from '../components/statical'
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
        [68.1, 79146, 'Tea'],
        [19.6, 91852, 'Orange Juice'],
        [10.6, 101852, 'Lemon Juice'],
        [32.7, 20112, 'Walnut Brownie']
      ]
    }
  },
  name: 'left',
  components: {
    piechart,
    statical
  }
}
</script>
<style>
.title{
    font-weight: 700;
    font-size: 20px;
    width: 200px;
    height: 60px;
    display: block;
    margin: 0 auto;
    color:white
}
</style>
