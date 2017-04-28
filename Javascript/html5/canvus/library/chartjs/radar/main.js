var drawGraph = function(data){
  var ctx = document.getElementById('graph').getContext('2d');
  // データ1
  var data1 = { 
    label:'今日', 
    data:data[1],
    backgroundColor: "rgba(250, 50, 50, 0.3)",
    borderColor: "rgba(200, 50, 50, 0.3)",
    pointHoverBackgroundColor: "rgba(200, 50, 50, 0.3)",
    pointHoverBorderColor: "rgba(200, 50, 50, 0.3)",
  };
  // データ2
  var data2 = {
    label:'昨日',
    data:data[2],
    backgroundColor: "rgba(50, 50, 250, 0.3)",
    borderColor: "rgba(50, 50, 200, 0.3)",
    pointHoverBackgroundColor: "rgba(50, 50, 200, 0.3)",
    pointHoverBorderColor: "rgba(50, 50, 200, 0.3)",
  }
  // ラベル(横軸)
  var label = data[0];

  // データの設定
  var config = {
    type: 'radar', // グラフの種類（レーダーチャートを指定）
    data: { labels: label, datasets: [data1, data2]}, 
  }
  var myChart = new Chart(ctx, config);

};


window.onload=function () {
    var data = [['12:00', '13:00', '14:00', '15:00', '16:00'],
                [22, 23, 21, 20, 19],
                [25, 23, 25, 23, 22]]
    drawGraph(data);
};