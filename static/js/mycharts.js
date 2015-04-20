require.config({
            paths: {
                echarts: 'static/js/echarts/dist'
            }
        });
        require(
            [
                'echarts',
                'echarts/chart/line', // 使用柱状图就加载bar模块，按需加载
                'echarts/chart/bar', // 使用柱状图就加载bar模块，按需加载
                'echarts/chart/radar', // 使用柱状图就加载bar模块，按需加载
                'echarts/chart/gauge', // 使用柱状图就加载bar模块，按需加载
            ],
            function (ec) {
                // 基于准备好的dom，初始化echarts图表
                var myChart1 = ec.init(document.getElementById('main1'));
                var myChart2 = ec.init(document.getElementById('main2'));
                var myChart3 = ec.init(document.getElementById('main3'));
                var myChart4 = ec.init(document.getElementById('main4')); 
                var option1 = {
    title: {
        x: 'center',
        text: 'ECharts例子个数统计',
        subtext: 'Rainbow bar example',
        link: 'http://echarts.baidu.com/doc/example.html'
    },
    tooltip: {
        trigger: 'item'
    },
    toolbox: {
        show: true,
        feature: {
            dataView: {show: true, readOnly: false},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    calculable: true,
    grid: {
        borderWidth: 0,
        y: 80,
        y2: 60
    },
    xAxis: [
        {
            type: 'category',
            show: false,
            data: ['Line', 'Bar', 'Scatter', 'K', 'Pie', 'Radar', 'Chord', 'Force', 'Map', 'Gauge', 'Funnel']
        }
    ],
    yAxis: [
        {
            type: 'value',
            show: false
        }
    ],
    series: [
        {
            name: 'ECharts例子个数统计',
            type: 'bar',
            itemStyle: {
                normal: {
                    color: function(params) {
                        // build a color map as your need.
                        var colorList = [
                          '#C1232B','#B5C334','#FCCE10','#E87C25','#27727B',
                           '#FE8463','#9BCA63','#FAD860','#F3A43B','#60C0DD',
                           '#D7504B','#C6E579','#F4E001','#F0805A','#26C0C0'
                        ];
                        return colorList[params.dataIndex]
                    },
                    label: {
                        show: true,
                        position: 'top',
                        formatter: '{b}\n{c}'
                    }
                }
            },
            data: [12,21,10,4,12,5,6,5,25,23,7],
            markPoint: {
                tooltip: {
                    trigger: 'item',
                    backgroundColor: 'rgba(0,0,0,0)',
                    formatter: function(params){
                        return '<img src="' 
                                + params.data.symbol.replace('image://', '')
                                + '"/>';
                    }
                },
                data: [
                    {xAxis:0, y: 350, name:'Line', symbolSize:20, symbol: 'image://../asset/ico/折线图.png'},
                    {xAxis:1, y: 350, name:'Bar', symbolSize:20, symbol: 'image://../asset/ico/柱状图.png'},
                    {xAxis:2, y: 350, name:'Scatter', symbolSize:20, symbol: 'image://../asset/ico/散点图.png'},
                    {xAxis:3, y: 350, name:'K', symbolSize:20, symbol: 'image://../asset/ico/K线图.png'},
                    {xAxis:4, y: 350, name:'Pie', symbolSize:20, symbol: 'image://../asset/ico/饼状图.png'},
                    {xAxis:5, y: 350, name:'Radar', symbolSize:20, symbol: 'image://../asset/ico/雷达图.png'},
                    {xAxis:6, y: 350, name:'Chord', symbolSize:20, symbol: 'image://../asset/ico/和弦图.png'},
                    {xAxis:7, y: 350, name:'Force', symbolSize:20, symbol: 'image://../asset/ico/力导向图.png'},
                    {xAxis:8, y: 350, name:'Map', symbolSize:20, symbol: 'image://../asset/ico/地图.png'},
                    {xAxis:9, y: 350, name:'Gauge', symbolSize:20, symbol: 'image://../asset/ico/仪表盘.png'},
                    {xAxis:10, y: 350, name:'Funnel', symbolSize:20, symbol: 'image://../asset/ico/漏斗图.png'},
                ]
            }
        }
    ]
};
                    
                var option2 = {
    tooltip : {
        formatter: "{a} <br/>{b} : {c}%"
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    series : [
        {
            name:'业务指标',
            type:'gauge',
            startAngle: 180,
            endAngle: 0,
            center : ['50%', '90%'],    // 默认全局居中
            radius : 320,
            axisLine: {            // 坐标轴线
                lineStyle: {       // 属性lineStyle控制线条样式
                    width: 200
                }
            },
            axisTick: {            // 坐标轴小标记
                splitNumber: 10,   // 每份split细分多少段
                length :12,        // 属性length控制线长
            },
            axisLabel: {           // 坐标轴文本标签，详见axis.axisLabel
                formatter: function(v){
                    switch (v+''){
                        case '10': return '低';
                        case '50': return '中';
                        case '90': return '高';
                        default: return '';
                    }
                },
                textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                    color: '#fff',
                    fontSize: 15,
                    fontWeight: 'bolder'
                }
            },
            pointer: {
                width:40,
                length: '70%',
                color: 'rgba(255, 255, 255, 0.8)'
            },
            title : {
                show : true,
                offsetCenter: [0, '-60%'],       // x, y，单位px
                textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                    color: '#fff',
                    fontSize: 30
                }
            },
            detail : {
                show : true,
                backgroundColor: 'rgba(0,0,0,0)',
                borderWidth: 0,
                borderColor: '#ccc',
                width: 80,
                height: 40,
                offsetCenter: [0, -40],       // x, y，单位px
                formatter:'{value}%',
                textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                    fontSize : 50
                }
            },
            data:[{value: 50, name: '完成率'}]
        }
    ]
};


timeTicket = setInterval(function (){
    option.series[0].data[0].value = (Math.random()*100).toFixed(2) - 0;
    myChart.setOption(option,true);
},2000)
                    
                var option3 = {
    title : {
        text: '罗纳尔多 vs 舍普琴科',
        subtext: '完全实况球员数据'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        x : 'center',
        data:['罗纳尔多','舍普琴科']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    polar : [
        {
            indicator : [
                { text : '语文', max  : 150 },
                { text : '数学', max  : 150 },
                { text : '英语', max  : 150 },
                { text : '物理', max  : 120 },
                { text : '化学', max  : 108 },
                { text : '生物', max  : 100 }
            ],
            center : ['50%', 210],
            radius : 150
        }
    ],
    series : [
        {
            name: '完全实况球员数据',
            type: 'radar',
            itemStyle: {
                normal: {
                    areaStyle: {
                        type: 'default'
                    }
                }
            },
            data : [
                {
                    value : [97, 42, 88, 94, 90, 86],
                    name : '舍普琴科'
                },
                {
                    value : [97, 32, 74, 95, 88, 92],
                    name : '罗纳尔多'
                }
            ]
        }
    ]
};
                    
                var option4 = {
    title : {
        text : '时间坐标折线图',
        subtext : 'dataZoom支持'
    },
    tooltip : {
        trigger: 'item',
        formatter : function (params) {
            var date = new Date(params.value[0]);
            data = date.getFullYear() + '-'
                   + (date.getMonth() + 1) + '-'
                   + date.getDate() + ' '
                   + date.getHours() + ':'
                   + date.getMinutes();
            return data + '<br/>'
                   + params.value[1] + ', ' 
                   + params.value[2];
        }
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    dataZoom: {
        show: true,
        start : 70
    },
    legend : {
        data : ['series1']
    },
    grid: {
        y2: 80
    },
    xAxis : [
        {
            type : 'time',
            splitNumber:10
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name: 'series1',
            type: 'line',
            showAllSymbol: true,
            symbolSize: function (value){
                return Math.round(value[2]/10) + 2;
            },
            data: (function () {
                var d = [];
                var len = 0;
                var now = new Date();
                var value;
                while (len++ < 200) {
                    d.push([
                        new Date(2014, 9, 1, 0, len * 10000),
                        (Math.random()*30).toFixed(2) - 0,
                        (Math.random()*100).toFixed(2) - 0
                    ]);
                }
                return d;
            })()
        }
    ]
};
        
                // 为echarts对象加载数据 
                myChart1.setOption(option1); 
                myChart2.setOption(option2); 
                myChart3.setOption(option3); 
                myChart4.setOption(option4); 
            }
        );