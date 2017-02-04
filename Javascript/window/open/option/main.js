function main()
{
    //中央に表示するための左上の座標を計算
    var left = ( screen.width-640 ) / 2;
    var top = ( screen.height-480 ) / 2;
	
    // URL
    var url = 'http://www.dmm.com/netgame_s/kancolle/';
    
    // ウィンドウのサイズ
    var size = 'width = 800, height = 600'; 
	
	  // ウィンドウの位置
	  var size = 'left = 0, top = 600'; 
	
	  // 各種バーの設定
	  var bar = 'scrollbars = yes, toolbar = no, menubar=yes, status=yes, directories=yes';
	
	  // その他の設定
	  var other = 'resizable=yes';
	
    // ウィンドウを表示
    window.open(url, '艦これ' , size + ', ' + loc + ', '  + bar + ', ' + other);
}
