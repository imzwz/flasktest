var myChart = echarts.init(document.getElementById('event-trend'));
        var base = +new Date(2014, 3, 5);
	var oneDay = 24 * 3600 * 1000;
	var date = [];

	var data = [Math.random() * 300];

for (var i = 1; i < 11; i++) {
    var now = new Date(base += oneDay);
    if(now.getDate()>=29&&now.getDate()<=31) {
    	//data.push(Math.round((Math.random() - 0.5) * 20 + data[i - 1]));
    	continue;
    }
    
    date.push([now.getFullYear(), now.getMonth(), now.getDate()].join('-'));
    data.push(Math.round((Math.random()) * 300 ));
    
}
data=[0,1,500,720,860,910,602,500,380]
option = {
    tooltip: {
        trigger: 'axis',
        position: function (pt) {
            return [pt[0], '10%'];
        }
    },
    title: {
        left: 'center',
        text: '马航mh370事件热度趋势图',
        textStyle:{
            color:'#000'
        }
    },
    legend: {
        top: 'bottom',
        data:['意向']
    },
    toolbox: {
        show: true,
        feature: {
            dataView: {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: date,
        textStyle:{
            color:'#000'
        }
    },
    yAxis: {
        type: 'value',
        boundaryGap: [0, '100%']
    },
    dataZoom: [{
        type: 'inside',
        start: 0,
        end: 10
    }, {
        start: 0,
        end: 10
    }],
    series: [
        {
            name:'热度',
            type:'line',
            smooth:true,
            symbol: 'none',
            sampling: 'average',
            itemStyle: {
                normal: {
                    color: 'rgb(255, 70, 131)'
                }
            },
            areaStyle: {
                normal: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: 'rgb(255, 158, 68)'
                    }, {
                        offset: 1,
                        color: 'rgb(255, 70, 131)'
                    }])
                }
            },
            data: data
        }
    ]
};
myChart.setOption(option); 
        