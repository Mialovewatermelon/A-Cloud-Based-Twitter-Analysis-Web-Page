<template>
    <div class='combine'>
        <dv-border-box-11 title="Twitter analysis">
        <combineData :combineInfo="combineInfo"></combineData>
        </dv-border-box-11>
    </div>
</template>

<script>
import combineData from '../part/combine'
export default {
  name: 'combine',
  data () {
    return {
      combineInfo: null
    }
  },
  mounted () {
    this.getCombineData()
    console.log('hi')
  },
  methods: {
    getCombineData () {
      this.axios.get('/api/tweet/get_combine_data').then(response => {
        this.loaded = true
        console.log(window.location.host)
        this.combineData = response.data
      })
    }
  },
  components: {
    combineData
  }
}
</script>

<style scoped>
.combine{
  width: 100%;
  height:100%;
  background-color: black;
}
</style>
