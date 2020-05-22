<template>
  <div id="piecharts2" class="agechart"></div>
</template>

<script>
export default {
  props: {
    ageData: {
      type: Array,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: [
        { value: 80, name: '云南' },
        { value: 5, name: '北京' },
        { value: 15, name: '山东' },
        { value: 25, name: '河北' },
        { value: 20, name: '江苏' },
        { value: 35, name: '浙江' },
        { value: 30, name: '四川' },
        { value: 40, name: '湖北' }
      ]
    }
  },

  data () {
    return {
      chart: null,
      option: null
    }
  },
  // 如果pieChartData 更新了值则需要刷新数据
  watch: {
    ageData: {
      handler (newVal, oldVal) {
        console.log('hello')
        if (this.ageData) {
          if (newVal) {
            this.option.series[0].data = newVal
            // this.option.legend.data = newVal.name
            this.chart.setOption(this.option, true)
          } else {
            this.option.series[0].data = this.oldVal
            // this.option.legend.data = this.oldVal.name
            this.chart.setOption(oldVal, true)
          }
        } else {
          this.init()
        }
      },
      deep: true // 对象内部属性的监听，关键。
    }
  },

  mounted () {
    this.drawECharts()
  },
  name: 'piechart2',
  methods: {
    drawECharts () {
      this.chart = this.$echarts.init(
        document.getElementById('piecharts2'),
        'temp'
      )
      this.option = {
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          left: 'center',
          top: 'bottom',
          data: this.ageData.name,
          textStyle: {
            color: 'white'
          }
        },
        toolbox: {
          show: true,
          feature: {
            mark: {show: true},
            magicType: {
              show: true,
              type: ['pie', 'funnel']
            }
          }
        },
        series: [
          {
            name: 'Age Distribution',
            type: 'pie',
            radius: [40, 150],
            center: ['50%', '30%'],
            roseType: 'area',
            label: {
              show: true
            },
            emphasis: {
              label: {
                show: true
              }
            },
            data: this.ageData
          }
        ]

      }

      if (this.option && typeof this.option === 'object') {
        this.chart.setOption(this.option, true)
        // window.addEventListener('resize', function () {
        //   this.chart.resize()
        // })
      }
    }
  }
}
</script>

<style scoped>
.agechart {
  width: 600px;
  height: 400px;
}
</style>
