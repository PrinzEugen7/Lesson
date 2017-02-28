function main()
{
    // インスタンス生成
    var date=new Date(); 
	
	// 曜日格納用の配列を初期化
    var weeks = new Array("日","月","火","水","木","金","土");

    // 年・月・日・曜日を取得
    var year = date.getFullYear();
    var month = date.getMonth()+1;
    var day = date.getDate();
    var week = weeks[ date.getDay() ];
    // 結果表示
    alert(year + "年" + month + "月" + day + "日 (" + week + ")");
}
