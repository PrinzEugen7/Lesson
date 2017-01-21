var loadBtn = document.querySelector("#loadBtn");
loadBtn.addEventListener('change', upload, false);

// アップロード時の処理
function upload(evt) {
    //alert("error");
	if (!isFileUpload()) {
		alert("エラー：FileAPI非対応のブラウザです。");
	} else {
		var data = null;
		// 選択されたファイル情報を取得
		var file = evt.target.files[0];
		var reader = new FileReader();
		// ファイル読み取りを実行
		reader.readAsText(file);
		// ファイルの内容を表示
		reader.onload = function(event) {
			var result = event.target.result;
			alert(result)
		};
		reader.onerror = function() {
			alert("エラー：ファイルをロードできません。");
		};
	}
}

// ファイルアップロード判定
function isFileUpload() {
	   var isCompatible = false;
	   if (window.File && window.FileReader && window.FileList && window.Blob) {
	   isCompatible = true;
	   }
	   return isCompatible;
}
