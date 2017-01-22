function main()
{
    // 文字列の宣言・初期化
    var str = "<b>にゃんぱすー</b>"
    // HTMLタグも含めて書き換え
	document.getElementById("nicovideo").innerHTML = str;
	alert(str);
}
