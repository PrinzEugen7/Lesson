function wareki2seireki(nengo, wareki)
{
    if ((nengo == "平成") && (wareki > 0)) 
    {
        return parseInt(wareki) + 1988;
    }
    else if ((nengo == "昭和") && (wareki > 0) && (wareki <= 64)) 
    {
        return parseInt(wareki) + 1925;
    }
    else if ((nengo == "大正") && (wareki > 0) && (wareki <= 15)) 
    {
        return parseInt(wareki) + 1911;
    }
    else if ((nengo == "明治") && (wareki > 0) && (wareki <= 45))
    {
        return parseInt(wareki) + 1867;
    }
    else{}
}

function seireki2wareki(year)
{
    if (year > 1988) 
    {
        return "平成" + (year - 1988);
    }
    else if (year > 1925) 
    {
        return "昭和" + (year - 1925);
    }
    else if (year > 1911) 
    {
        return "大正" + (year - 1911);
    }
    else if (year > 1988)
    {
        return "明治" + (year - 1867);
    }
    else{}
}


// 初期化
function createAssArray(min, max)
{
  var srcArray = [];
  // srcArrayにmin～maxまでの値を挿入
        for(var i = min; i <= max; i++)
        {  
        srcArray[i] = i + '年';   
        }
        return srcArray;
}


function setSelect( idName, elementName, menu )
{
    // 入力ボックスの値を取得
    var id = document.getElementById(idName);

    // メニュー項目のセット
    for ( var i in menu ) 
    {
        var element = document.createElement(elementName);
        element.setAttribute('value', i);
        element.innerHTML = menu[i];
        id.appendChild( element );
    }
}

// 初期化
function init()
{
    // 連想配列
    var nengo = {
        '昭和' : '昭和',
        '大正' : '大正',
        '明治' : '明治'
    };
	var nengoYear = createAssArray(2, 62);
	var seirekiYear = createAssArray(1931, 2017);
    // selectの初期化
    setSelect( 'nengo', 'option', nengo );
    setSelect( 'nengoYear', 'option', nengoYear );
    setSelect( 'seirekiYear', 'option', seirekiYear );
}

// 西暦→和暦
function ToWareki()
{
    // 入力ボックスの値を取得
    var seireki = document.toWareki.seireki.value;
    wareki = seireki2wareki(seireki);
	var result = "西暦" + seireki + "年 → " + wareki + "年"
    // 結果表示
	document.result.box.value = result + "\n" + document.result.box.value;

}

// 和暦→西暦
function ToSeireki()
{
    // 入力ボックスの値を取得
    var nengo = document.toSeireki.nengo.value;	
    var nengoYear = document.toSeireki.nengoYear.value;
    seireki = wareki2seireki(nengo, nengoYear);
	result = nengo + nengoYear +"年 → 西暦" + seireki + "年"
    // 結果表示
	document.result.box.value = result + "\n" + document.result.box.value;
}
