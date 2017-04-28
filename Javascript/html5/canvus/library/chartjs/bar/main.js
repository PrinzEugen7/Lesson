var drawGraph = function(data){
  var ctx = document.getElementById('graph').getContext('2d');
  // 棒1
  var data1 = { 
    label:'今日', 
    data:data[1],
    backgroundColor: "#DE4E33",
    borderColor: "#DE4E33",
    pointHoverBackgroundColor: "#DE4E33",
    pointHoverBorderColor: "#DE4E33",
  };
  // 棒2
  var data2 = {
    label:'昨日',
    data:data[2],
    backgroundColor: "#97DBF2",
    borderColor: "#97DBF2",
    pointHoverBackgroundColor: "#97DBF2",
    pointHoverBorderColor: "#97DBF2",
  }
  // ラベル(横軸)
  var label = data[0];
  // x軸, y軸の設定
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
    type: 'bar', // グラフの種類（棒グラフを指定）
    data: { labels: label, datasets: [data1, data2]},
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
