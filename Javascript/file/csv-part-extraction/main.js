function csvToArray(path) {
  var csvData = new Array();
  var data = new XMLHttpRequest();        
  data.open("GET", path, false);
  data.send(null);
  var LF = String.fromCharCode(10);
  var lines = data.responseText.split(LF);
  for (var i = 0; i < lines.length;++i) {
    var cells = lines[i].split(",");
    if( cells.length != 1 ) {
      csvData.push(cells);
    }
  }
  return csvData;
}

function getDateData(date, src) {
  var dst = new Array();
  for(var i = 0; i < src.length; i++)
  if (src[i][0].indexOf(date) !== -1) {
    dst.push(src[i]);
  }
  return dst;
};

// ページロード時に実行
window.onload = function () {
  var csvData = csvToArray("data.csv");
  date = "2016-12-12";
  var data2 = getDateData(date, csvData);
  alert(data2);
};
