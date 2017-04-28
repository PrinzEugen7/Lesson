var drawGraph = function(data){
  var ctx = document.getElementById('graph').getContext('2d');
  var datas = {
    labels: data[0],
    datasets: [{
      backgroundColor: ["rgba(200,20,20,0.3)","rgba(20,200,20,0.3)","rgba(20,20,200,0.3)"],
      hoverBackgroundColor: ["rgba(250,20,20,0.3)","rgba(20,250,20,0.3)","rgba(20,20,250,0.3)"],
      data: data[1]
    }]
  };
  var config = {
    type: 'pie',
    data: datas
  };
  var myChart = new Chart(ctx, config);
};


window.onload=function () {
    var data = [['A', 'B', 'C'],
                [200, 100, 50]]
    drawGraph(data);
};
