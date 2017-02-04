function main()
{
    //中央に表示するための左上の座標を計算
    var left = ( screen.width-640 ) / 2;
    var top = ( screen.height-480 ) / 2;
	
    // URL
    var url = 'http://www.dmm.com/netgame_s/kancolle/';
	
	// ウィンドウのサイズ
	var width = 800;
	var height = 600;
	
    // ウィンドウを表示
    window.open(url, '艦これトップ' , 'width=' + width + ', ' + 'height=' + height + ', ' + ', left=' + left+',top=' + top);
}

