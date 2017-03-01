// 年齢算出（生年月日）
function calcAge(year, month, day) {
        var birthdate = year * 10000 + month * 100 + day;
        var today = new Date();
        var targetdate = today.getFullYear() * 10000 + (today.getMonth() + 1) * 100 + today.getDate();
        return (Math.floor((targetdate - birthdate) / 10000));
}

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
function createAssArray(min, max, end)
{
  var srcArray = [];
  // srcArrayにmin～maxまでの値を挿入
        for(var i = min; i <= max; i++)
        {  
        srcArray[i] = i + end;   
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
        '西暦' : '西暦',
        '昭和' : '昭和',
        '大正' : '大正',
        '明治' : '明治'
    };

    // selectの初期化
    var month = createAssArray(2, 12, '月');
    var day = createAssArray(2, 31, '日');
    // selectの初期化
	setSelect( 'nengo', 'option', nengo );
    setSelect( 'month', 'option', month );
    setSelect( 'day', 'option', day );
}

// 初期化
function setYear()
{
	clearSelect();
    var nengo = document.inputData.nengo.value;

    if(nengo =="西暦")
	{
        var year = createAssArray(1945, 2016, '年');
        setSelect( 'year', 'option', year.sort(function(a,b){return(b-a);})  );

	}
    else if(nengo =="平成")
	{
        var year = createAssArray(1, 29, '年');
        setSelect( 'year', 'option', year.sort(function(a,b){return(b-a);})  );

	}
    else if(nengo =="昭和")
	{
        var year = createAssArray(1, 64, '年');
        setSelect( 'year', 'option', year.sort(function(a,b){return(b-a);})  );

	}
    else if(nengo =="大正")
	{
        var year = createAssArray(1, 15, '年');
        setSelect( 'year', 'option', year.sort(function(a,b){return(b-a);})  );

	}
    else if(nengo =="明治")
	{
        var year = createAssArray(1, 45, '年');
        setSelect( 'year', 'option', year.sort(function(a,b){return(b-a);})  );

	}
	else{ }
}

function clearSelect()
{

	var len = document.inputData.year.length;
	if(len > 1) {
		//optionsの配列番号にnullを入れることでデータが削除されます。
		document.form1.select1.options[len - 1] = null;
	}
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

function main()
{
    // 生年月日を変数に格納
    var year = 1994; 
        var month = 4;
        var day = 16;
   // 生年月日から現在の年齢を計算
    age = calcAge(year, month, day)
    // 結果表示
    alert("現在年齢：" + age);
}



function main()
{
    // 選択アイテムの値を取得
    name = document.formName.selectName.value;
    // 表示
    alert(name);
}
