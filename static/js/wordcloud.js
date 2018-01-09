var myChart = echarts.init(document.getElementById('word-cloud'));

    function createRandomItemStyle() {
        return {
            normal: {
                color: 'rgb(' + [
                    Math.round(Math.random() * 255),
                    Math.round(Math.random() * 255),
                    Math.round(Math.random() * 255)
                ].join(',') + ')'
            }
        };
    }

    option = {
        title: {
        	left: 'center',
            text: '',
            link: '',
            textStyle:{
                color:'#000'
            }
            
        },
        tooltip: {
            show: true
        },
        series: [{
            name: 'keywords',
            type: 'wordCloud',
            size: ['80%', '80%'],
            textRotation : [0, 45, 90, -45],
            textPadding: 0,
            autoSize: {
                enable: true,
                minSize: 14
            },
            data: [
                {
                    name: "马航",
                    value: 10000,
                    itemStyle: {
                        normal: {
                            color: '#000'
                        }
                    }
                },
                {
                    name: "MH370",
                    value: 6181,
                    itemStyle: createRandomItemStyle()
                },
                {
                    name: "马来西亚",
                    value: 4386,
                    itemStyle: createRandomItemStyle()
                },
                {
                    name: "航班",
                    value: 4055,
                    itemStyle: createRandomItemStyle()
                },
                {
                    name: "消失",
                    value: 2467,
                    itemStyle: createRandomItemStyle()
                },
                {
                    name: "失踪",
                    value: 1677,
                    itemStyle: createRandomItemStyle()
                },
                {
                    name: "飞机",
                    value: 1576,
                    itemStyle: createRandomItemStyle()
                },
                {
                    name: "乘客",
                    value: 1484,
                    itemStyle: createRandomItemStyle()
                },
                {
                    name: "祈祷",
                    value: 1312,
                    itemStyle: createRandomItemStyle()
                },
                {
                    name: "失联",
                    value: 965,
                    itemStyle: createRandomItemStyle()
                },
                {
                    name: "降落",
                    value: 847,
                    itemStyle: createRandomItemStyle()
                },
                {
                    name: "波音",
                    value: 1265,
                    itemStyle: createRandomItemStyle()
                }
            ]
        }]
    };                           
    myChart.setOption(option);    