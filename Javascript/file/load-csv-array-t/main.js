// CSVファイル読み込み
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

function arrayT(array){
  var arrayT = [];
  for (var i = 0; i < array.length; i++) {
    for (var j = 0; j < array[i].length; j++) {
      (i > 0)? arrayT[j].push(array[i][j]) :arrayT[j] = [array[i][j]];
    }
  }
  return arrayT;
}

// ページロード時に実行
window.onload=function () {
    var data = csvToArray("data.csv");
    var dataT = arrayT(data);
    alert(dataT[0]);
};
