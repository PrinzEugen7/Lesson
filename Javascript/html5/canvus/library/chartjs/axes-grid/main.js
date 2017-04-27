
var drawGraph = function(data){
  var ctx = document.getElementById('graph').getContext('2d');
  // 折れ線1
  var line1 = { 
    label:'今日', 
    data:data[1],
    fill: false,
    lineTension: 0,
    backgroundColor: "#DE4E33",
    borderColor: "#DE4E33",
    pointHoverBackgroundColor: "#DE4E33",
    pointHoverBorderColor: "#DE4E33",
  };
  // 折れ線2
  var line2 = {
    label:'昨日',
    data:data[2],
    fill: false,
    lineTension: 0,
    backgroundColor: "#97DBF2",
    borderColor: "#97DBF2",
    pointHoverBackgroundColor: "#97DBF2",
    pointHoverBorderColor: "#97DBF2",
  }
  // ラベル(横軸)
  var label = data[0];

  var xAxes = [{ 
    gridLines:{
      color: "#5f5f5f",
    },
    ticks: {
      fontColor: "#aaa",
      fontSize: 15,
    }
  }]
  var yAxes = [{ 
    gridLines:{
      color: "#5f5f5f",
    },
    ticks: {
      fontColor: "#aaa",
      fontSize: 15,
    }
  }]
       var scales = {xAxes, yAxes};
  // グラフ全体の設定
  var option = {scales};
  // データの設定
  var config = {
    type: 'line',
    data: { labels: label, datasets: [line1, line2]},
    options: option,
    
  }
  var myChart = new Chart(ctx, config);

};


window.onload=function () {
    var data = [['12:00', '13:00', '14:00', '15:00', '16:00'],
                [22, 23, 21, 20, 19],
                [25, 23, 25, 23, 22]]
    drawGraph(data);
};
