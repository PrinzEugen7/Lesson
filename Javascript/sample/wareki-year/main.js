function setSelect( idName, elementName, menu )
{
    // 入力ボックスの値を取得
    var id = document.getElementById('select');

    // メニュー項目のセット
    for ( var i in menu ) 
    {
        var element = document.createElement('option');
        element.setAttribute('value', i);
        element.innerHTML = menu[i];
        id.appendChild( element );
    }
}

function wareki2year(nengo, wareki)
{
    if ((nengo == "平成") && (wareki > 0)) 
    {
        return wareki + 1988;
    }
    else if ((nengo == "昭和") && (wareki > 0) && (wareki <= 64)) 
    {
        return wareki + 1925;
    }
    else if ((nengo == "大正") && (wareki > 0) && (wareki <= 15)) 
    {
        return wareki + 1911;
    }
    else if ((nengo == "明治") && (wareki > 0) && (wareki <= 45))
    {
        return wareki + 1867;
    }
    else{}
}


function year2wareki(year)
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
function init()
{
    // 連想配列
    var nengo = {
        '平成' : '平成',
        '昭和' : '昭和',
        '大正' : '大正',
        '明治' : '明治'
    };
    // selectの初期化
    setSelect( 'nengo', 'option', nengo );
}

function ToWareki()
{
    // 入力ボックスの値を取得
    var year = document.year.select.value;
    // 結果表示
    var wareki = year2wareki(year);
	    // 和暦を西暦に変換
    alert(wareki);
}

function ToYear()
{
    // 入力ボックスの値を取得
    var nengo = document.wareki.nengo.value;
    var num = document.wareki.num.value;
	    // 和暦を西暦に変換
    year = wareki2year(nengo, num);
    alert(year);
}
