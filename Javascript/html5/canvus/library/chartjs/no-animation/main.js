
var drawGraph = function(data){
  var ctx = document.getElementById('graph').getContext('2d');
  // 折れ線1
  var line1 = { 
        label:'今日', data:data[1],
        fill: false,
        backgroundColor: "rgba(200,30,30,0.4)",
        borderColor: "rgba(230,10,10,1)",
        lineTension: 0,
        pointHoverBackgroundColor: "rgba(75,192,192,1)",
        pointHoverBorderColor: "rgba(220,220,220,1)",
  };
  // 折れ線2
  var line2 = {
    label:'昨日',
    fill:false, 
    data:data[2]
  }
  // ラベル(横軸)
  var label = data[0];
  // グラフ全体の設定
  var option = {
    animation: false
  };
  // データの設定
  var config = {
    type: 'line',
    data: { labels: label, datasets: [line1, line2]},
    options: option
  }
  var myChart = new Chart(ctx, config);

};


window.onload=function () {
    var data = [['12:00', '13:00', '14:00', '15:00', '16:00'],
                [22, 23, 21, 20, 19],
                [55, 50, 45, 43, 42]]
    drawGraph(data);
};
