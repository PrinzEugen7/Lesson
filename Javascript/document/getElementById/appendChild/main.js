function main()
{
    // 文字列の宣言・初期化
	  var code = "alert('にゃんぱすー')";
    // HTMLタグも含めて書き換え
    var script=document.createElement('script');
    script.innerHTML = code;
    document.getElementById('nicovideo').appendChild(script);
}
