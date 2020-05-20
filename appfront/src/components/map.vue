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
    name: "map",
    props:{
        mapName:{
            type:String,
            default: 'state.json'
        },
        mapData: {
            type: Array,
        },
        mapTitle:{
            type:Map
        },
        maxValue:{
            type:Number
        },

    },
    data() {
        return {
            mapAddress: '/components/' + this.mapName
        };
    },
    mounted() {
        this.initMap()
        // this.setMarker();
    },
    methods: {

        // 建立地圖
        initMap() {

            let myChart = this.$echarts.init(document.getElementById("map"))
            myChart.showLoading();

            // eslint-disable-next-line no-undef
            this.$axios.get(this.mapAddress).then((response) => {

                myChart.hideLoading();
                console.log(response)
                let features = response.data.features
                console.log(response)
                features.forEach((element) => {
                    element.properties.name = element.properties.STATE_NAME
                })
                response.data.features = features
                // eslint-disable-next-line no-unused-vars
                    this.$echarts.registerMap('vic', response.data)
                // eslint-disable-next-line no-unused-vars



                    let option = {
                        // title: {
                        //     text: 'USA Population Estimates (2012)',
                        //     subtext: 'Data from www.census.gov',
                        //     sublink: 'http://www.census.gov/popest/data/datasets.html',
                        //     left: 'right'
                        // },
                        title: this.mapTitle,
                        tooltip: {
                            trigger: 'item',
                            showDelay: 0,
                            transitionDuration: 0.2,
                            formatter: function (params) {
                                var value = (params.value + '').split('.');
                                value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,');
                                return params.seriesName + '<br/>' + params.name + ': ' + value;
                            }
                        },
                        visualMap: {
                            left: 'right',
                            min: 0,
                            max: this.minValue,
                            inRange: {
                                color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
                            },
                            text: ['High', 'Low'],           // 文本，默认为数值文本
                            calculable: true
                        },
                        toolbox: {
                            show: true,
                            //orient: 'vertical',
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
                                name: 'victoria area',
                                type: 'map',
                                roam: true,
                                map: 'vic',
                                emphasis: {
                                    label: {
                                        show: true
                                    }
                                },
                                // 文本位置修正
                                textFixed: {
                                    Alaska: [20, -20]
                                },
                                data: this.mapData
                            }
                        ]
                    };
                    if (option && typeof option === "object") {
                        myChart.setOption(option, true)
                    }

            })

        },
    }
};
</script>

<style scoped>
    .google-map{
        width : 500px;
        height : 300px;
    }
</style>
