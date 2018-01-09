var myChart = echarts.init(document.getElementById('event-map'));
 	 function randomData() {
            return Math.round(Math.random()*1000);
        }

        option = {
            /*
            title: {
                text: '马航MH370微博地域分布',
                left: 'center',
                textStyle:{
                    color: '#000'
                }
            },
            */
            tooltip: {
                trigger: 'item'
            },
            legend: {
                orient: 'vertical',
                left: 'left',
                data:[{
                    name:'微博数',
                    icon:'circle',
                    textStyle: {color: '#000'}
                }],
                testStyle:{
                    color: '#000'
                }
            },
            visualMap: {
                min: 0,
                max: 2500,
                left: 'left',
                top: 'bottom',
                text: ['高','低'],           // 文本，默认为数值文本
                calculable: true
            },
            toolbox: {
                show: true,
                orient: 'vertical',
                left: 'right',
                top: 'center',
                feature: {
                    dataView: {readOnly: false},
                    restore: {},
                    saveAsImage: {}
                }
            },
            series: [
                {
                    name: '微博数',
                    type: 'map',
                    mapType: 'china',
                    roam: false,
                    textStyle:{
                      color: '#fff'  
                    },
                    label: {
                        normal: {
                            show: true
                        },
                        emphasis: {
                            show: true
                        }
                    },
                    data:[
                        {name: '北京',value: 1793 },
                        {name: '天津',value: 347 },
                        {name: '上海',value: 2209 },
                        {name: '重庆',value: 560 },
                        {name: '河北',value: 802 },
                        {name: '河南',value: 707 },
                        {name: '云南',value: 746 },
                        {name: '辽宁',value: 418 },
                        {name: '黑龙江',value: 451 },
                        {name: '湖南',value: 676 },
                        {name: '安徽',value: 714 },
                        {name: '山东',value: 849 },
                        {name: '新疆',value: 551 },
                        {name: '江苏',value: 677 },
                        {name: '浙江',value: 1384 },
                        {name: '江西',value: 717 },
                        {name: '湖北',value: 777 },
                        {name: '广西',value: 419 },
                        {name: '甘肃',value: 217 },
                        {name: '山西',value: 426 },
                        {name: '内蒙古',value: 329 },
                        {name: '陕西',value: 768 },
                        {name: '吉林',value: 237 },
                        {name: '福建',value: 987 },
                        {name: '贵州',value: 347 },
                        {name: '广东',value: 1377 },
                        {name: '青海',value: 54 },
                        {name: '西藏',value: 25 },
                        {name: '四川',value: 554 },
                        {name: '宁夏',value: 562 },
                        {name: '海南',value: 346 },
                        {name: '台湾',value: 217 },
                        {name: '香港',value: randomData() },
                        {name: '澳门',value: randomData() }
                    ]
                },
               
                
            ]
        };
        myChart.setOption(option);   
