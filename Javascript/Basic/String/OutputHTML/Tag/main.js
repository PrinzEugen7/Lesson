function main()
{
    // 文字列の宣言・初期化
    var str = "<script type=\"text/javascript\" src=\"http://ext.nicovideo.jp/thumb_watch/sm29483618\"></script>";
    // HTMLタグも含めて書き換え
	document.getElementById("nicovideo").innerHTML = str;
}
