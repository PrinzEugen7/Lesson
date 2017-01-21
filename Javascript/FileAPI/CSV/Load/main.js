function main(){
	var result = document.getElementById('result');
	var select = document.getElementById('select');

	// ファイルが選択されたとき
	select.addEventListener('change', function(e) {
		// 選択されたファイルの情報を取得
		var fileData = e.target.files[0];

		var loader = new FileReader();
		// ロード失敗時
		loader.onerror = function() {
			alert("ファイルを正常に取得できませんでした。");
		}
		// ロード成功時
		loader.onload = function() {
			// 行単位で配列にする
			var lineArr = loader.result.split("\n");
			// 行と列の二次元配列にする
			var itemArr = [];
			for (var i = 0; i < lineArr.length; i++) {
				itemArr[i] = lineArr[i].split(",");
			}

			// tableで出力
			var insert = '<table>';
			for (var i = 0; i < itemArr.length; i++) {
				insert += '<tr>';
				for (var j = 0; j < itemArr[i].length; j++) {
					insert += '<td>';
					insert += itemArr[i][j];
					insert += '</td>';
				}
				insert += '</tr>';
			}
			insert += '</table>';
			result.innerHTML = insert;
		}

		// ファイル読み取りを実行
		loader.readAsText(fileData);
	}, false);
}
