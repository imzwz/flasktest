var myChart = echarts.init(document.getElementById('device'));
option = {
    		title:{
    			/*text:"微博文本长度分布统计",*/
    			/*text:"马航MH370用户客户端分布",*/
    			left:"center",
                textStyle:{
                    color:'#000'
                }
    		},
    	    tooltip: {
    	        trigger: 'item',
    	        formatter: "{a} <br/>{b}: {c} ({d}%)"
    	    },
    	    legend: {
    	        orient: 'vertical',
    	        x: 'left',
     	        data:['新浪微博','专业版微博','皮皮时关机','iPhone客户端','Android客户端','iPad客户端','媒体版微博','其他']  	    
//				data:['<20','20-40','40-60','60-80','80-100','100-120','>120']
    	    },
    	    series: [
    	       
    	        {
    	            name:'访问来源',
    	            type:'pie',
    	            radius: [0, '55%'],

    	            data:[
    	                {value:1526, name:'专业版微博'},
    	                {value:8000, name:'新浪微博'},
    	                {value:3000, name:'iPhone客户端'},
    	                {value:1004, name:'iPad客户端'},
    	                {value:2000, name:'媒体版微博'},
    	                {value:1304, name:'皮皮时光机'},
    	                {value:7800, name:'Android客户端'},
                        {value:3029, name:'其他'}
    	            ]
    	        }
    	    ]
    };
myChart.setOption(option);
