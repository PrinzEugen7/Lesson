function main()
{
    // 配列を宣言・初期化
    data = new Array('沖田', '武蔵', 'モードレッド');
	  // 処理
    result = data.shift();
	  // 結果表示
    alert( result +"\n" + data);
}
